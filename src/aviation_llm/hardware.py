from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class HardwareType(str, Enum):
    CPU = "cpu"
    GPU = "gpu"
    NPU = "npu"


@dataclass
class HardwareProfile:
    kind: HardwareType
    max_memory_gb: int | None = None
    recommended_batch_size: int = 1
    recommended_dtype: str = "float16"
    notes: str = ""


def get_hardware_profile(kind: str | HardwareType) -> HardwareProfile:
    normalized = HardwareType(kind.lower()) if isinstance(kind, str) else kind

    if normalized == HardwareType.CPU:
        return HardwareProfile(
            kind=HardwareType.CPU,
            max_memory_gb=32,
            recommended_batch_size=1,
            recommended_dtype="float32",
            notes="경량 검증 및 로컬 서빙에 적합",
        )
    if normalized == HardwareType.GPU:
        return HardwareProfile(
            kind=HardwareType.GPU,
            max_memory_gb=48,
            recommended_batch_size=4,
            recommended_dtype="bfloat16",
            notes="대규모 학습 및 빠른 추론에 적합",
        )
    return HardwareProfile(
        kind=HardwareType.NPU,
        max_memory_gb=16,
        recommended_batch_size=1,
        recommended_dtype="int8",
        notes="경량 온디바이스 추론 및 민감정보 로컬 처리에 적합",
    )


__all__ = ["HardwareType", "HardwareProfile", "get_hardware_profile"]
