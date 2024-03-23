import os
from pathlib import Path
from typing import Callable, Optional, Any, Set

import yaml
from nonebot import logger
from pydantic import BaseModel

from typing_extensions import Literal

pack_name = __package__


def _ensure_dir(path: Path) -> None:
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
    elif not path.is_dir():
        raise RuntimeError(f"{path} is not a directory")


def _auto_create_dir(func: Callable[..., Path]) -> Callable[..., Path]:
    def wrapper(*args, **kwargs) -> Path:
        path = func(*args, **kwargs)
        _ensure_dir(path)
        return path

    return wrapper


class ConfigManager(BaseModel):
    BASE_CONFIG_DIR: Optional[Path] = None
    BASE_DATA_DIR: Optional[Path] = None
    BASE_CACHE_DIR: Optional[Path] = None
    plugin_name: Optional[str] = ""

    def __init__(self, plugin_name: str):
        super().__init__()
        WORKSPACE_PATH = os.getcwd()
        self.plugin_name = plugin_name
        self.BASE_CACHE_DIR = Path(
            os.path.join(WORKSPACE_PATH, "cache")
        )

        self.BASE_CONFIG_DIR = Path(
            os.path.join(WORKSPACE_PATH, "configs")
        )

        self.BASE_DATA_DIR = Path(
            os.path.join(WORKSPACE_PATH, "data")
        )

    @_auto_create_dir
    def get_cache_dir(self) -> Path:
        return Path(os.path.join(self.BASE_CACHE_DIR, self.plugin_name)) if self.plugin_name else self.BASE_CACHE_DIR

    def get_cache_file(self, filename: str) -> Path:
        return Path(os.path.join(self.get_cache_dir(self.plugin_name), filename))

    @_auto_create_dir
    def get_config_dir(self) -> Path:
        return Path(os.path.join(self.BASE_CONFIG_DIR, self.plugin_name)) if self.plugin_name else self.BASE_CONFIG_DIR

    def get_config_file(self, filename: str) -> Path:
        return Path(os.path.join(self.get_config_dir(), filename))

    @_auto_create_dir
    def get_data_dir(self) -> Path:
        return Path(os.path.join(self.BASE_DATA_DIR, self.plugin_name)) if self.plugin_name else self.BASE_DATA_DIR

    def get_data_file(self, filename: str) -> Path:
        return Path(os.path.join(self.get_data_dir(), filename))

    def save_config(self, file_name: str, data: dict) -> None:
        if not self.get_config_dir(self.plugin_name).exists():
            logger.error("配置目录未设置。")
            return
        save_path = os.path.join(self.get_config_dir(self.plugin_name), file_name + "yaml")

        try:
            with open(save_path, 'w', encoding='utf-8') as file:
                yaml.dump(data, file, default_flow_style=False)
            logger.info(f"配置文件已经保存到 {save_path}")
        except PermissionError:
            logger.error(f"没有权限写入到 {save_path}")
        except IOError as e:
            logger.error(f"写入配置文件时发生错误 {save_path}")
        except Exception as e:
            logger.error(f"保存配置文件发生未知错误: \n{save_path}")

    def model_dump(
            self,
            *,
            mode: Literal['json', 'python'] | str = 'python',
            include=None,
            exclude=None,
            by_alias: bool = False,
            exclude_unset: bool = False,
            exclude_defaults: bool = False,
            exclude_none: bool = False,
            round_trip: bool = False,
            warnings: bool = True,
    ) -> dict[str, Any]:
        default_exclude = {"BASE_CONFIG_DIR", "BASE_CACHE_DIR", "BASE_DATA_DIR", "plugin_name"}
        if exclude is None:
            exclude = default_exclude
        else:
            exclude.update(default_exclude)  # 将默认排除的字段加入到已提供的排除字段中
        result = super().model_dump(exclude=exclude)
        return result

    def load_config_yaml(self, file_name) -> dict:
        path = os.path.join(self.get_config_dir(), file_name + '.yaml')
        with open(path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
        return data
