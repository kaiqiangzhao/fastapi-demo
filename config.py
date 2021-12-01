#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kaiqiang.zhao

from pydantic import BaseSettings

"""
config文件没有放到app/core文件夹内
runserver内需要setting
因为app外的py文件不能引用app内的包
app内的可以引用app外的包, 避免耦合
"""


class Settings(BaseSettings):
    app_name: str = "FastApiDemo"
    database_url: str
    debug: bool
    web_dir_path: str

    host: str
    port: int

    class Config:
        env_file = ".env"


settings = Settings()
