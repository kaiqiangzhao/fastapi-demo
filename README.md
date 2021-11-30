# fastapi-demo

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

website: https://fastapi.tiangolo.com/

### 技术架构

开发语言: Python

框架: FastApi

### 快速开始

环境 :重命名 `.env.example` 为 `.env`

启动

```shell script
uvicorn app.main:app --reload
```

迁移 

新建model, 需要导入到`app/models/base.py`文件内

表的migrate可以执行下面的命令，-m类似git的注释，可自行修改

如果是第一次执行，需要在alembic文件下新建`versions`文件夹，存放迁移记录文件
```shell script
alembic revision --autogenerate -m "init commit"
alembic upgrade head 
```

自动生成的接口文档：http://127.0.0.1:8000/docs

### 目录结构
```
.
├── README.md
├── alembic  // 迁移脚本和迁移生成的migration文件
│   ├── README
│   ├── env.py
│   └── script.py.mako
├── alembic.ini  // 数据迁移配置文件
├── app
│   ├── __init__.py
│   ├── const     // 常量
│   ├── core      // 核心配置
│   ├── curd      // 对数据的增删改查
│   ├── main.py   // 项目启动
│   ├── manager   // 通用的业务逻辑代码，如发短信
│   ├── model     // 数据层
│   ├── router   // url映射
│   ├── schema   // 转换前端传过来的参数
│   └── service  // 业务层
├── docs  // 文档相关，不用可删除
├── requirements.txt  // 环境依赖
├── utils  // 系统工具包, 如生成随机数
│   └── __init__.py
└── web
    └── index.html
```
项目共分为四层：router -> service -> curd -> model

也可以将curd和model合并，将curd的代码写到model，但一定要保证一个py文件只保护一个model的定义，否则之后文件代码增长的很快

### 其他
#### Uvicorn
Uvicorn is a lightning-fast ASGI server implementation, using uvloop and httptools. Uvicorn 是基于 uvloop 和 httptools 构建的非常快速的 ASGI 服务器。

学习资料: https://www.uvicorn.org/ https://zhuanlan.zhihu.com/p/115237857

#### Alembic
alembic是sqlalchemy的作者开发的。用来做OMR模型与数据库的迁移与映射。

官方文档：https://alembic.sqlalchemy.org/en/latest/

