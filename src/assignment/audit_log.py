"""
Assignment 11 — Audit Log starter (TODO).

Records every interaction for forensics. Never blocks by itself —
other layers catch attacks; this layer makes them reviewable.
"""
from __future__ import annotations

import json
import time
from datetime import datetime, timezone
from pathlib import Path


def default_audit_log_path() -> str:
    """Always resolve to <repo>/outputs/… (safe when cwd is src/)."""
    repo_root = Path(__file__).resolve().parents[2]
    return str(repo_root / "outputs" / "audit_log.json")


class AuditLogPlugin:
    """Framework-agnostic audit logger (wire into ADK callbacks or your pipeline)."""

    def __init__(self):
        self.name = "audit_log"
        self.logs: list[dict] = []
        self._open: dict[str, float] = {}

    def record_input(self, *, user_id: str, text: str, request_id: str | None = None):
        """Store the request start without writing an incomplete audit row."""
        key = request_id or str(user_id)
        self._open[key] = {
            "user_id": str(user_id),
            "request_id": request_id,
            "input": text or "",
            "started_at": utc_now_iso(),
            "started_monotonic": time.perf_counter(),
        }
        return key

    def record_output(
        self,
        *,
        user_id: str,
        text: str,
        blocked: bool = False,
        layer: str | None = None,
        request_id: str | None = None,
    ):
        """Close an interaction and append one complete, reviewable audit row."""
        key = request_id or str(user_id)
        opened = self._open.pop(key, None)
        started = opened.get("started_monotonic") if opened else None
        latency_ms = (
            round((time.perf_counter() - started) * 1000, 3)
            if started is not None
            else None
        )
        row = {
            "timestamp": utc_now_iso(),
            "user_id": str(user_id),
            "request_id": request_id,
            "input": opened.get("input", "") if opened else "",
            "output": text or "",
            "blocked": bool(blocked),
            "layer": layer,
            "started_at": opened.get("started_at") if opened else None,
            "latency_ms": latency_ms,
        }
        self.logs.append(row)
        return row

    def export_json(self, filepath: str | None = None):
        """Write logs to disk (JSON array) under repo-root ``outputs/`` by default."""
        path = Path(filepath or default_audit_log_path())
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(self.logs, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        return path


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()
