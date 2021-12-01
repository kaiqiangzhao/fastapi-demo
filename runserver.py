#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kaiqiang.zhao

import uvicorn
from config import settings


"""
启动服务
根目录下执行 `python runserver.py` 
TODO: host和post可传入
"""

if __name__ == '__main__':
    uvicorn.run(
        app="app.main:app",
        host=settings.host,
        port=settings.port,
        reload=True if settings.debug else False
    )