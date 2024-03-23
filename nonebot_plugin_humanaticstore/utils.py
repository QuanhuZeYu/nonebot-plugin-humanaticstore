import shutil
from pathlib import Path


def show_dir_detail(dir: Path):
    """
    命令行方法
    传入目录 Path 打印 制表 Type | Size | Name
    :param dir:
    :return:
    """
    print(f"Directory: {dir}")
    # 如果不存在直接返回
    if not dir.exists():
        return
    # 制表 1-类型 2-大小 3-名称
    print("Type\tSize\tName")
    for f in dir.iterdir():
        # 如果遍历的元素是目录 则 1 显示为 d
        if f.is_dir():
            print("dir", end="\t")
        # 如果遍历元素使文件 则 1 显示为 -
        elif f.is_file():
            print("file", end="\t")
        # 如果遍历元素既不是文件也不是目录 则 1显示为 ?
        else:
            print("?", end="\t")
        # 2 显示 大小
        print(f.stat().st_size, end="\t")
        # 3 显示名称
        print(f.name)


def remove_dir(dir: Path):
    """
    命令行方法
    传入 Path 交互式提示是否删除 交互命令行输入 y yes 1 则进行删除

    删除方式为递归删除目录
    :param dir:
    :return:
    """
    # 如果目录存在
    if dir.exists():
        # 交互式提示是否删除 默认 N
        confirm = input(f"Are you sure to clear {dir}? [y/N] ")
        # 输入默认换为小写 如果存在 y yes 1 则进行删除 递归删除目录
        if confirm.lower() in {"y", "yes", "1"}:
            shutil.rmtree(dir)
