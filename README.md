# fastapi-demo

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

website: https://fastapi.tiangolo.com/

### 技术架构

开发语言: Python

框架: FastApi

### 快速开始

启动

```shell script
uvicorn app.main:app --reload
```

迁移 

新建model, 需要导入到`app/models/base.py`文件内

```shell script
alembic revision --autogenerate -m "init commit"
alembic upgrade head 
```
