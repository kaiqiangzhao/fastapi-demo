#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kaiqiang.zhao

from fastapi import FastAPI
from app.routers.api import router
from app.core.config import settings


def create_app() -> FastAPI:
    application = FastAPI(title=settings.app_name)
    application.include_router(router=router)
    return application


app = create_app()
