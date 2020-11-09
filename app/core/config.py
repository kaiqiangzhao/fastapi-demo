#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kaiqiang.zhao

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "EggHunt"
    database_url: str

    class Config:
        env_file = ".env.example"


settings = Settings()
