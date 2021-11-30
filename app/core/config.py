#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kaiqiang.zhao

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "FastApiDemo"
    database_url: str
    web_dir_path: str

    class Config:
        env_file = ".env"


settings = Settings()
