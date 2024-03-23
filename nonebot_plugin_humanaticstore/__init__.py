from nonebot import get_plugin_config, logger
from nonebot.plugin import PluginMetadata

from .config import Config

__plugin_meta__ = PluginMetadata(
    name="人类友好数据配置",
    description="存储插件数据至nb_cli所在相对路径",
    usage=(
        '声明依赖: `require("nonebot_plugin_humanaticstore")`\n'
        '实例化对象: ConfigManager(plugin_name)'
        "导入所需文件夹:\n"
        '  `cache_dir = store.get_cache_dir("plugin_name")`\n'
        '  `cache_file = store.get_cache_file("plugin_name", "file_name")`\n'
        '  `data_dir = store.get_data_dir("plugin_name")`\n'
        '  `data_file = store.get_data_file("plugin_name", "file_name")`\n'
        '  `config_dir = store.get_config_dir("plugin_name")`\n'
        '  `config_file = store.get_config_file("plugin_name", "file_name")`'
    ),
    type="library",
    homepage="https://github.com/QuanhuZeYu/nonebot-plugin-humanaticstore",
    config=Config,
)

from .config_manager import ConfigManager

plugin_config = get_plugin_config(Config)

config_manager = ConfigManager("nonebot_plugin_humanaticstore")
config_dir = config_manager.get_config_dir()
config_data = config_manager.model_dump()
BASE_CACHE_DIR = config_manager.BASE_CACHE_DIR
BASE_DATA_DIR = config_manager.BASE_DATA_DIR
BASE_CONFIG_DIR = config_manager.BASE_CONFIG_DIR

logger.info(f"基础 Cache 目录: {BASE_CACHE_DIR}")
logger.info(f"基础 Data 目录:  {BASE_DATA_DIR}")
logger.info(f"基础 Config 目录:{BASE_CONFIG_DIR}")
