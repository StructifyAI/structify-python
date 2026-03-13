# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["SandboxGetMetricsResponse", "Memory", "Process", "Sandbox"]


class Memory(BaseModel):
    available_mb: float

    percent: float

    total_mb: float

    used_mb: float


class Process(BaseModel):
    cpu_percent: float

    memory_mb: float


class Sandbox(BaseModel):
    remaining_seconds: int

    start_time: float

    total_timeout_seconds: int

    uptime_seconds: int


class SandboxGetMetricsResponse(BaseModel):
    cpu_percent: float

    memory: Memory

    process: Process

    sandbox: Sandbox
