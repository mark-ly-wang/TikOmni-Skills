#!/usr/bin/env python3
"""Minimal MCP HTTP client for social-media-crawl."""

from __future__ import annotations

import json
import urllib.request
from dataclasses import dataclass
from typing import Any, Dict, Optional


def _parse_response_body(body: bytes) -> Any:
    text = body.decode("utf-8", errors="replace").strip()
    if not text:
        return {}
    if text.startswith("data:"):
        payloads = []
        for line in text.splitlines():
            if not line.startswith("data:"):
                continue
            payload = line.split("data:", 1)[1].strip()
            if payload:
                payloads.append(payload)
        if payloads:
            return json.loads(payloads[-1])
    return json.loads(text)


@dataclass
class McpResponse:
    ok: bool
    status_code: int
    data: Any
    session_id: Optional[str]
    error_reason: Optional[str] = None


class McpHttpClient:
    def __init__(self, *, url: str, api_key: str, timeout_ms: int = 60000) -> None:
        self.url = url.rstrip("/")
        self.api_key = api_key
        self.timeout_ms = timeout_ms
        self.session_id: Optional[str] = None
        self._next_id = 1

    def _headers(self) -> Dict[str, str]:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
            "User-Agent": "OpenClaw-SocialMediaCrawl/0.1",
            "X-Client-Name": "social-media-crawl",
            "X-Client-Version": "0.1.0",
        }
        if self.session_id:
            headers["mcp-session-id"] = self.session_id
        return headers

    def _request(self, payload: Dict[str, Any]) -> McpResponse:
        req = urllib.request.Request(
            self.url,
            data=json.dumps(payload).encode("utf-8"),
            headers=self._headers(),
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=max(self.timeout_ms / 1000.0, 1.0)) as response:
                body = response.read()
                data = _parse_response_body(body)
                session_id = response.headers.get("mcp-session-id") or response.headers.get("Mcp-Session-Id")
                if session_id:
                    self.session_id = session_id
                return McpResponse(ok=True, status_code=response.getcode(), data=data, session_id=self.session_id)
        except urllib.error.HTTPError as error:
            body = error.read()
            try:
                data = _parse_response_body(body)
            except Exception:
                data = {"raw": body.decode("utf-8", errors="replace")}
            return McpResponse(
                ok=False,
                status_code=error.code,
                data=data,
                session_id=self.session_id,
                error_reason=f"http_error:{error.code}",
            )
        except Exception as error:
            return McpResponse(
                ok=False,
                status_code=0,
                data={},
                session_id=self.session_id,
                error_reason=f"request_failed:{type(error).__name__}:{error}",
            )

    def _rpc(self, method: str, params: Optional[Dict[str, Any]] = None, notification: bool = False) -> McpResponse:
        payload: Dict[str, Any] = {"jsonrpc": "2.0", "method": method}
        if not notification:
            payload["id"] = self._next_id
            self._next_id += 1
        if params is not None:
            payload["params"] = params
        return self._request(payload)

    def initialize(self) -> McpResponse:
        response = self._rpc(
            "initialize",
            {
                "protocolVersion": "2025-03-26",
                "capabilities": {},
                "clientInfo": {"name": "social-media-crawl", "version": "0.1.0"},
            },
        )
        if response.ok:
            self._rpc("notifications/initialized", notification=True)
        return response

    def tools_list(self) -> McpResponse:
        if not self.session_id:
            init = self.initialize()
            if not init.ok:
                return init
        return self._rpc("tools/list")

    def tool_call(self, name: str, arguments: Optional[Dict[str, Any]] = None) -> McpResponse:
        if not self.session_id:
            init = self.initialize()
            if not init.ok:
                return init
        return self._rpc("tools/call", {"name": name, "arguments": arguments or {}})

    def catalog_search(self, query: str) -> McpResponse:
        return self.tool_call("catalog.search", {"query": query})

    def endpoint_describe(self, method: str, path: str) -> McpResponse:
        return self.tool_call("endpoint.describe", {"method": method, "path": path})

    def api_call(
        self,
        method: str,
        path: str,
        query: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None,
        body: Optional[Any] = None,
    ) -> McpResponse:
        return self.tool_call(
            "api.call",
            {
                "method": method,
                "path": path,
                "query": query or {},
                "headers": headers or {},
                "body": {} if body is None else body,
            },
        )

    def u2_submit(self, file_url: str) -> McpResponse:
        return self.tool_call("u2.submit", {"file_url": file_url})

    def u2_query(self, task_id: str) -> McpResponse:
        return self.tool_call("u2.query", {"task_id": task_id})
