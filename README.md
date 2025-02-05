# rye-env

@[TOC](目录)
# Rye完整使用教学

> [官方网址](https://rye.astral.sh/): https://rye.astral.sh/

## 主题总结：

1. **Rye 安装与配置**
   * 安装`rye`工具并配置环境。
   * 配置`pyproject.toml`和锁定文件`rye.lock`。
2. **Rye 工作区 (****`workspaces`****)**
   * 创建、切换和管理工作区。
   * 为不同的开发环境或 CI 环境使用独立的工作区。
3. **虚拟环境管理 (****`virtual`****)**
   * 创建、激活、查看和删除虚拟环境。
   * 使用虚拟环境隔离项目依赖。
4. **依赖管理与安装 (****`deps`****)**
   * 使用`rye add`添加依赖。
   * 管理不同的依赖类型（普通依赖、开发依赖等）。
5. **同步依赖 (****`sync`****)**
   * 使用`rye sync`同步项目的依赖。
   * 使用`--with-sources`选项来包含源代码文件。
6. **全局工具与命令 (****`shims`****)**
   * 安装并使用全局命令（shims）来简化工具管理。
   * 查看和卸载全局工具。
7. **发布项目 (****`publish`****)**
   * 使用`rye publish`将 Python 项目发布到包管理平台（如 PyPI）。
8. **Rust 集成 (****`rust`****)**
   * 在`rye`中安装和使用 Rust 工具链。
   * 在 Python 项目中集成 Rust 扩展。
9. **Docker 与 Rye 集成**
   * 在 Docker 中配置和使用`rye`，管理依赖和虚拟环境。
10. **配置源仓库 (****`sources`****)**
    * 添加、删除和查看项目的依赖源仓库。
    * 配置和管理私有或自定义源。

***

### 1.Rye 安装与配置

* **安装&#x20;****`rye`**：
  * 使用以下命令在系统中安装`rye`：`curl -sSL https://rye.astral.sh/get.sh | bash `
    * `windows` 直接 安装官网提供的: [rye-x86\_64-windows.exe](https://github.com/astral-sh/rye/releases/latest/download/rye-x86_64-windows.exe)
    ```
    curl -sSL https://rye.astral.sh/get.sh | bash
    ```
* **配置项目**：
  * 初始化一个新的 Python 项目：`rye init `
    ```
    rye init
    ```
* **查看&#x20;****`pyproject.toml`****&#x20;文件**：
  * 这是项目的主要配置文件，其中定义了依赖、工具链等。

***

### 2.Rye 工作区 (`workspaces`)

* **创建工作区**：
  * 创建一个新的工作区：`rye workspace new <workspace-name> `
    ```
    rye workspace new <workspace-name>
    ```
* **切换工作区**：
  * 切换到一个已有的工作区：`rye workspace use <workspace-name> `
    ```
    rye workspace use <workspace-name>
    ```
* **查看当前工作区**：
  * 查看当前激活的工作区：`rye workspace `
    ```
    rye workspace
    ```
* **删除工作区**：
  * 删除一个工作区：`rye workspace remove <workspace-name> `
    ```
    rye workspace remove <workspace-name>
    ```

***

### 3.虚拟环境管理 (`virtual`)

* **创建虚拟环境**：
  * 创建一个新的虚拟环境：`rye virtual new <env-name> `
    ```
    rye virtual new <env-name>
    ```
* **激活虚拟环境**：
  * 激活某个虚拟环境：`rye virtual use <env-name> `
    ```
    rye virtual use <env-name>
    ```
* **查看所有虚拟环境**：
  * 列出所有虚拟环境：`rye virtual list `
    ```
    rye virtual list
    ```
* **删除虚拟环境**：
  * 删除某个虚拟环境：`rye virtual remove <env-name> `
    ```
    rye virtual remove <env-name>
    ```

***

### 4.依赖管理与安装 (`deps`)

* **添加依赖**：
  * 将依赖包添加到项目中：`rye add <package-name> `
    ```
    rye add <package-name>
    ```
* **添加开发依赖**：
  * 将依赖添加为开发依赖（如测试框架）：`rye add <package-name> --dev `
    ```
    rye add <package-name> --dev
    ```
* **指定版本的依赖**：
  * 安装特定版本的依赖：`rye add <package-name>==<version> `
    ```
    rye add <package-name>==<version>
    ```

***

### 5.同步依赖 (`sync`)

* **同步项目的依赖**：
  * 同步项目依赖并安装所有缺少的包：`rye sync `
    ```
    rye sync
    ```
* **使用&#x20;****`--with-sources`****&#x20;同步源代码**：
  * 在同步时包括源代码文件：`rye sync --with-sources `
    ```
    rye sync --with-sources
    ```

***

### 6.全局工具与命令 (`shims`)

* **安装全局工具**：
  * 使用`rye`安装全局工具（例如，格式化工具`black`）：`rye install black `
    ```
    rye install black
    ```
* **查看已安装的全局工具**：
  * 列出所有安装的全局工具：`rye list `
    ```
    rye list
    ```
* **卸载全局工具**：
  * 卸载一个全局工具：`rye uninstall black `
    ```
    rye uninstall black
    ```

***

### 7.发布项目 (`publish`)

* **构建项目**：
  * 在发布前，先构建项目：`rye build `
    ```
    rye build
    ```
* **发布到 PyPI**：
  * 将项目发布到 PyPI 或其他包仓库：`rye publish `
    ```
    rye publish
    ```
* **配置 PyPI 登录**：
  * 配置 PyPI 的认证信息：`pysetup config pypi `
    ```
    pysetup config pypi
    ```

***

### 8.Rust 集成 (`rust`)

* **安装 Rust 工具链**：
  * 使用`rye`安装 Rust 工具链：`rye toolchain install rust `
    ```
    rye toolchain install rust
    ```
* **为 Python 项目配置 Rust**：
  * 将 Rust 集成到 Python 项目中，通常用于构建本地扩展：`rye toolchain use rust `
    ```
    rye toolchain use rust
    ```

***

### 9.Docker 与 Rye 集成

* **安装 Rye 到 Docker 容器中**：
  * 在 Dockerfile 中安装`rye`：`RUN curl -sSL https://rye.astral.sh/get.sh | bash `
    ```
    RUN curl -sSL https://rye.astral.sh/get.sh | bash
    ```
* **同步项目依赖**：
  * 在 Dockerfile 中同步项目依赖：`COPY pyproject.toml . COPY rye.lock . RUN rye sync `
    ```
    COPY pyproject.toml .
    COPY rye.lock .
    RUN rye sync
    ```
* **运行项目**：
  * 在 Docker 容器中运行 Python 项目：`CMD ["rye", "run", "python", "main.py"] `
    ```
    CMD ["rye", "run", "python", "main.py"]
    ```

***

### 10.配置源仓库 (`sources`)

* **添加源仓库**：
  * 为项目添加自定义的依赖源：`rye sources add <source-url> `
    ```
    rye sources add <source-url>
    ```
* **查看所有配置的源**：
  * 列出所有已添加的源：`rye sources list `
    ```
    rye sources list
    ```
* **删除源仓库**：
  * 删除某个源：`rye sources remove <source-url> `
    ```
    rye sources remove <source-url>
    ```

***

## 完整项目使用案例

> 基于`fastapi`开发项目，采用格式化工具，并配置镜像源加速，最后配合`pyinstaller `进行项目打包，还要给出 rye script的使用（采用 `rye run build-exe` 打包exe，采用 `rye run web` 运行fastapi项目，采用 `rye run lint` 进行代码检查， 采用 `rye run format` 进行项目代码格式化）

下面是一个完整的 **FastAPI** 项目案例，演示如何使用`rye`来管理整个项目的开发流程，包括初始化项目、安装依赖、使用格式化工具、配置清华源加速、打包成 EXE 文件等。

### 1. 项目初始化

首先，初始化一个新的**FastAPI**项目，并使用`rye`来管理依赖和工具。

#### 步骤：

1. **创建新项目目录**： 在终端中创建一个新的项目目录并进入该目录
   ```
   mkdir fastapi_project
   cd fastapi_project
   ```
2. **初始化项目**： 使用`rye`初始化 Python 项目
   ```
   rye init
   ```
3. **初始化&#x20;****`rye.lock`****&#x20;文件**
   ```
   rye sync
   ```

***

### 2. 安装依赖

我们需要安装以下依赖：

* `fastapi`: FastAPI 框架。
* `uvicorn`: ASGI 服务器，用于运行 FastAPI 应用。
* `black`: 代码格式化工具。
* `flake8`: 代码检查工具。
* `pyinstaller`: 用于打包成 EXE 文件。

#### 步骤：

1. **安装 FastAPI 和 Uvicorn**：`rye add fastapi uvicorn `
   ```shell
   rye add fastapi uvicorn
   ```
2. **安装格式化工具（Black）和代码检查工具（Flake8）**：`rye add black flake8 --dev `
   ```shell
   rye add black flake8 --dev
   ```
3. **安装 PyInstaller 用于打包 EXE 文件**：`rye add pyinstaller --dev `
   ```shell
   rye add pyinstaller --dev
   ```
4. **配置清华源加速**：编辑`pyproject.toml`文件，配置 PyPI 镜像源为阿里镜像。`rye`在安装依赖时会使用清华源加速下载。
   ```toml
   [[tool.rye.sources]]
	name = "default"
	url = "https://mirrors.aliyun.com/pypi/simple/"
   ```

***

### 3. 创建 FastAPI 应用

创建一个简单的 FastAPI 应用，`main.py`文件如下：

```python
"""
    main.py
"""

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.fastapi_project.main:app", host="0.0.0.0", port=8000, reload=False)
```

这个应用只有一个根路径`/`，返回一条简单的 JSON 消息。

***

### 4. 配置 Rye 脚本

`rye`支持使用自定义脚本来简化操作。我们可以在`pyproject.toml`文件中配置脚本，用于运行不同的命令，如构建 EXE、运行 FastAPI 服务、代码格式化、代码检查等。

#### 修改`pyproject.toml`配置脚本：

```toml
# pyproject.toml
[tool.rye.scripts]
web = "uvicorn src.fastapi_project.main:app --reload"
# 如果需要使用到其他模块 => --hidden-import pandas | --noconsole
build-exe = "pyinstaller --onefile --add-data 'src/fastapi_project:src/fastapi_project' src/fastapi_project/main.py"
lint = "flake8"
format = "black ."

[[tool.rye.sources]]
name = "default"
url = "https://mirrors.aliyun.com/pypi/simple/"
```

***

### 5. 使用 Rye 命令管理项目

#### 运行 FastAPI 服务：

你可以使用`rye run web`命令来运行 FastAPI 项目：

```shell
rye run web
```

这将启动`uvicorn`服务器，并使 FastAPI 应用在`http://127.0.0.1:8000`可用。你可以在浏览器中访问`http://127.0.0.1:8000`来查看返回的 JSON 消息。

#### 格式化代码：

使用`rye run format`来格式化代码：

```shell
rye run format
```

这个命令将会使用`black`来格式化项目中的所有 Python 文件。

#### 进行代码检查：

使用`rye run lint`来进行代码检查：

```shell
rye run lint
```

这将使用`flake8`对项目中的 Python 文件进行检查，报告潜在的代码问题和风格问题。

#### 打包项目为 EXE 文件：

使用`rye run build-exe`来打包项目：

```shell
rye run build-exe
```

这个命令将使用`pyinstaller`打包项目文件`main.py`为一个独立的 EXE 文件。生成的 EXE 文件将在`dist/`目录中，运行后会启动与`uvicorn`一样的 FastAPI 服务。

***

### 6. 完整的`pyproject.toml`文件示例

以下是完整的`pyproject.toml`文件示例：

```toml
[project]
name = "fastapi-project"
version = "0.1.0"
description = "Add your description here"
authors = [
    { name = "fromsko", email = "1614355756@qq.com" }
]
dependencies = [
    "fastapi>=0.115.6",
    "uvicorn>=0.34.0",
    "pandas>=2.2.3",
]
readme = "README.md"
requires-python = ">= 3.8"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.rye]
managed = true
dev-dependencies = [
    "black>=24.10.0",
    "flake8>=7.1.1",
    "pyinstaller>=6.11.1",
]

[tool.hatch.metadata]
allow-direct-references = true

[tool.hatch.build.targets.wheel]
packages = ["src/fastapi_project"]

[tool.rye.scripts]
web = "uvicorn src.fastapi_project.main:app --reload"
# 如果需要使用到其他模块 => --hidden-import pandas | --noconsole
build-exe = "pyinstaller --onefile --add-data 'src/fastapi_project:src/fastapi_project' src/fastapi_project/main.py"
lint = "flake8"
format = "black ."

[[tool.rye.sources]]
name = "default"
url = "https://mirrors.aliyun.com/pypi/simple/"
```

***

### 7. 完整的项目目录结构

项目的目录结构可能如下：

```text
fastapi_project/
├─.python-version
├─pyproject.toml
├─README.md
├─requirements-dev.lock
├─requirements.lock
└─src
  └─fastapi_project
        ├─main.py        
        └__init__.py
```

***

### 8. 使用命令总览

* **启动 FastAPI 服务**：`rye run web `
  ```
  rye run web
  ```
* **格式化项目代码**：`rye run format `
  ```
  rye run format
  ```
* **进行代码检查**：`rye run lint `
  ```
  rye run lint
  ```
* **打包成 EXE 文件**：`rye run build-exe `
  ```
  rye run build-exe
  ```

***

### 总结


以上展示了如何使用`rye`管理一个基于 FastAPI 的 Python 项目，包括：

1. 初始化项目和安装依赖。
2. 使用`rye`脚本简化常见操作（如启动服务、格式化代码、代码检查、打包 EXE）。
3. 配置清华源加速。
4. 使用`pyinstaller`将项目打包为 EXE 文件。

通过这种方式，`rye`提供了一个简单、统一的工具链来管理项目的依赖、构建、测试和部署流程。
