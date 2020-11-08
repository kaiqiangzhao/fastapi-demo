#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kaiqiang.zhao

from fastapi import FastAPI
from app.controllers.api import router as api_router
from config import config


def create_application() -> FastAPI:
    application = FastAPI(title=config.PROJECT_NAME, debug=config.DEBUG, version=config.PROJECT_VERSION)
    application.include_router(router=api_router)
    return application


app = create_application()
