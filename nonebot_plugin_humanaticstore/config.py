from pathlib import Path
from typing import Optional

from pydantic import BaseModel


class Config(BaseModel):
    cache_dir: Optional[Path] = None
    config_dir: Optional[Path] = None
    data_dir: Optional[Path] = None
