<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-template

_✨ NoneBot 插件简单描述 ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/owner/nonebot-plugin-template.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-template">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-template.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>


一个更加用户友好的配置插件（工具集），目前只适合开发者使用，后续我会开发一个自动读取所有插件可配置项并自动导出
（通过官方读取的实现方式序列化导出）
<br>该项目改装自 **[localstore](https://github.com/nonebot/plugin-localstore)**

<details>
<summary>模板库使用方法</summary>

1. 点击仓库中的 "Use this template" 按钮, 输入仓库名与描述, 点击 "  Create repository from template" 创建仓库
2. 在创建好的新仓库中, 在 "Add file" 菜单中选择 "Create new file", 在新文件名处输入`LICENSE`, 此时在右侧会出现一个 "Choose a license template" 按钮, 点击此按钮选择开源协议模板, 然后在最下方提交新文件到主分支
3. 全局替换`owner`为仓库所有者ID; 全局替换`nonebot-plugin-template`为插件名; 全局替换`nonebot_plugin_template`为包名; 修改 python 徽标中的版本为你插件的运行所需版本
4. 修改 README 中的插件名和插件描述, 并在下方填充相应的内容

</details>

<details>
<summary>配置发布工作流</summary>

模块库中自带了一个发布工作流, 你可以使用此工作流自动发布你的插件到 pypi

> [!IMPORTANT]
> 这个发布工作流需要 pyproject.toml 文件, 并且只支持 [PEP 621](https://peps.python.org/pep-0621/) 标准的 pyproject.toml 文件

1. 前往 https://pypi.org/manage/account/#api-tokens 并创建一个新的 API 令牌。创建成功后不要关闭页面，不然你将无法再次查看此令牌。
2. 在单独的浏览器选项卡或窗口中，打开 [Actions secrets and variables](./settings/secrets/actions) 页面。你也可以在 Settings - Secrets and variables - Actions 中找到此页面。
3. 点击 New repository secret 按钮，创建一个名为 `PYPI_API_TOKEN` 的新令牌，并从第一步复制粘贴令牌。

</details>

<details>
<summary>触发发布工作流</summary>
从本地推送任意 tag 即可触发。

创建 tag:

    git tag <tag_name>

推送本地所有 tag:

    git push origin --tags

</details>

## 📖 行为介绍

此插件会根据你的 `nb_cli` 位置获得工作目录 `WORKSPACE`，随后使用`WORKSPACE`该字段
拼接出 `config` `data` `cache` 目录到工作目录下。

## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-humanaticstore

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-humanaticstore
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-humanaticstore
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-humanaticstore
</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-humanaticstore
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_humanaticstore"]

</details>

## ⚙️ 这么做的目的

更易于多个nonebot在同一个计算机或设备下，使用多种不同的配置，甚至你可以使用localstore
插件和本插件同时工作，由于本插件遵循面对对象的工作原则，只有实例化对象并使用对象和其他数据交互才有可能出现bug。


## 🎉 使开发者如何使用

首先，导入本包 `import nonebot_plugin_humanaticstore`
运行中导入时会自动获取nb_cli运行目录，
然后你就可以使用
`BASE_CACHE_DIR`
`BASE_DATA_DIR`
`BASE_CONFIG_DIR`
字段直接获取数据目录的 ***绝对路径***

编写配置可以直接使用python对象-字典；
通过导入
`from nonebot_plugin_humanaticstore import ConfigManger`
先获取配置管理对象，
对象内也拥有基础路径字段可提供使用，
#### 对象内常用方法
1. `get`_`config/data/cache` _ `file/dir`
***file*** 方法中需要 **文件名参数** *需要后缀*

2. `model_dump` 导出这个类中设置的所有字段，以python字典的形式导出

3. `save_config` **参数:** `文件名` 不需要后缀，强制为yaml格式; `data` 形如 *model_dump* 的字典格式
<br>将 data 存入 文件中

4. `load_config_yaml` **参数** `文件名` 不需要后缀 强制为 *yaml* ; 
<br>读取文件中的配置 ***返回*** python字典对象

5. `parse_obj` **参数** 字典
<br>用于更新对象中的字段
<br>标准用法放入解包的原始对象字典，再放入解包的新对象 -> <br>{**config_manger.dict(), **new_data}
建议先处理重复字段
```python
# 自定义更新逻辑的示例
for key, value in new_data.items():
    if hasattr(config, key):
        # 如果需要特殊处理重复字段，可以在这里实现
        # 例如，合并列表，选择保留原始值等
        pass
    else:
        # 如果字段不在原始配置中，直接设置新值
        setattr(config, key, value)
```
### 后话

如果各位有需要想实现的功能，可以咨询我<br>
邮箱: [1624910218@qq.com]() ~~只是做成了链接样式点不了的~~
### 效果图
如果有效果图的话
