#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kaiqiang.zhao
from fastapi import FastAPI
from app.controllers.api import router as api_router
from settings import PROJECT_NAME, PROJECT_DEBUG, PROJECT_VERSION, API_PREFIX


def create_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=PROJECT_DEBUG, version=PROJECT_VERSION)
    application.include_router(router=api_router, prefix=API_PREFIX)
    return application


app = create_application()