#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kaiqiang.zhao

import os
from fastapi import FastAPI
from app.router.api import router
from app.core.config import settings
from fastapi.staticfiles import StaticFiles


def create_app() -> FastAPI:
    application = FastAPI(title=settings.app_name)
    application.include_router(router=router)
    return application


app = create_app()

# 静态文件URL前缀为static, html内需要使用"../static"或"/static"
app.mount("/static", StaticFiles(directory=os.path.join(settings.web_dir_path, "static")), name="static")  # 挂载静态文件，指定目录
