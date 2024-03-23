from typing import Callable
from argparse import ArgumentParser

from .utils import remove_dir, show_dir_detail
from . import BASE_DATA_DIR, BASE_CACHE_DIR, BASE_CONFIG_DIR


# main function
def show_dir():
    """
    直接打印localstore获取到的 `cahe` `config` `data` 目录位置

    无返回值
    :return:
    """
    print("Cache Dir: ", BASE_CACHE_DIR)
    print("Config Dir: ", BASE_CONFIG_DIR)
    print("Data Dir: ", BASE_DATA_DIR)


def show_cache():
    """
    打印出 `cache` 的 Type | Size | Name
    :return:
    """
    show_dir_detail(BASE_CACHE_DIR)


def clear_cache():
    remove_dir(BASE_CACHE_DIR)


def show_config():
    show_dir_detail(BASE_CONFIG_DIR)


def clear_config():
    remove_dir(BASE_CONFIG_DIR)


def show_data():
    show_dir_detail(BASE_DATA_DIR)


def clear_data():
    remove_dir(BASE_DATA_DIR)


"""
以下命令行部分代码逻辑概要
[顶层节点nb localstore]
解析器对象: parser
注册默认方法: show_dir
注册子解析器对象: subparsers

[subparsers]
注册子解析器对象: [cache, config, data]
注册指令及其对应帮助: 
{
    cache: cache directory [--help]
    config: config directory [--help]
    data: data directory [--help]
}

[cache]
注册默认方法: show_cache
注册标题: [subcommand]
注册子解析器对象: [cache_subparsers]

    [cache_subparsers]
    注册命令及其帮助: {clear: clear_cache}
    注册命令对象: [cache_clear]
    
    [cache_clear]
    注册默认方法: [clear_cache]

[config]
注册标题: [subcommand]
注册默认方法: [show_config]
注册子解析器对象: [config_subparsers]

    [config_subparsers]
    注册指令及其帮助: {clear: clear_config [--help]}
    注册命令对象: [config_clear]
    
    [config_clear]
    注册默认方法: [config_clear]
    
[data]
注册标题: [subcommand]
注册默认方法: [data_config]
注册子解析器对象: [data_subparsers]

    [data_subparsers]
    注册指令及其帮助: {clear: clear_data [--help]}
    注册命令对象: [data_clear]
    
    [data_clear]
    注册默认方法: [data_clear]
"""
# 构建一个 名为nb localstore 的参数解析器
parser = ArgumentParser("nb humanstore")
# 为解析器设置默认方法 show_dir
parser.set_defaults(func=show_dir)

# sub parsers
# 添加子命令的解析器 command
subparsers = parser.add_subparsers(title="command")

# 在子解析器command下设置 cache 命令的解析器
cache = subparsers.add_parser("cache", help="cache directory")
# 添加子命令的解析器 cache sub ，针对 cache 命令
cache_subparsers = cache.add_subparsers(title="subcommand")

# 为 cache 命令设置默认函数
cache.set_defaults(func=show_cache)

# 添加 clear 子命令到 cache 命令
cache_clear = cache_subparsers.add_parser("clear", help="clear cache")

# 为 clear 子命令设置默认函数
cache_clear.set_defaults(func=clear_cache)

# 对 config 和 data 命令重复上述步骤，分别设置它们的默认函数和子命令
# config 命令的解析器
config = subparsers.add_parser("config", help="config directory")
config_subparsers = config.add_subparsers(title="subcommand")

config.set_defaults(func=show_config)

config_clear = config_subparsers.add_parser("clear", help="clear config")

config_clear.set_defaults(func=clear_config)

# data parser
data = subparsers.add_parser("data", help="data directory")
data_subparsers = data.add_subparsers(title="subcommand")

data.set_defaults(func=show_data)

data_clear = data_subparsers.add_parser("clear", help="clear data")

data_clear.set_defaults(func=clear_data)


def main():
    result = parser.parse_args()
    result = vars(result)
    prompt: Callable[..., None] = result.pop("func")
    prompt(**result)


if __name__ == "__main__":
    main()
