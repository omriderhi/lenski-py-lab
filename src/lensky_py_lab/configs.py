import os
from typing import Dict, Optional

from pydantic_settings import BaseSettings


class SourceConfig(BaseSettings):
    relevant_min: Optional[float] = None
    relevant_max: Optional[float] = None
    outlier_window: Optional[int] = None
    images_per_month: Optional[int] = None
    general_factor: Optional[float] = None
    data_header: Optional[str] = "NDVI"

    @classmethod
    def from_env_prefix(cls, prefix: str) -> "SourceConfig":
        filtered_env = {
            key[len(prefix):]: value
            for key, value in os.environ.items()
            if key.startswith(prefix)
        }
        return cls(**filtered_env)


class PlotsColourConfigurations(BaseSettings):
    default: str
    SATs: Dict[str, str]
    MATA_NDVI: Dict[str, str]
    RH_NDVI: Dict[str, str]
    IMS: Dict[str, str]
