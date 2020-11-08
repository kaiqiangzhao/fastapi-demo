#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kaiqiang.zhao

import os
from configparser import ConfigParser


class BaseConfig:
    BASE_ENV_CONFIG_PATH = "configs/env.ini"
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))

    def __init__(self):
        _config = ConfigParser()
        _config.read(os.path.join(self.BASE_DIR, self.BASE_ENV_CONFIG_PATH), encoding="utf-8")
        self._config = _config

    @property
    def ENVIRONMENT(self):
        return self._config.get("base", "env")


class Config(BaseConfig):
    ENV_CONFIG_PATH = "production"

    def __init__(self):
        super(Config, self).__init__()
        self._config.read(os.path.join(self.BASE_DIR, self.ENV_CONFIG_PATH), encoding="utf-8")

    @property
    def PROJECT_NAME(self):
        return self._config.get("project", "name")

    @property
    def DEBUG(self):
        return self._config.getboolean("project", "debug")

    @property
    def PROJECT_VERSION(self):
        return self._config.get("project", "version")

    @property
    def DATABASE_URL(self):
        return self._config.get("database", "url")

    @property
    def HOST(self):
        return self._config.get("project", "host")

    @property
    def PORT(self):
        return self._config.getint("project", "port")


class DevelopmentConfig(Config):
    ENV_CONFIG_PATH = "configs/dev.ini"

    
class TestingConfig(Config):
    ENV_CONFIG_PATH = "configs/test.ini"


class ProductionConfig(Config):
    ENV_CONFIG_PATH = "configs/prd.ini"


env_cfg_hash = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}


base_config = BaseConfig()
config = env_cfg_hash.get(base_config.ENVIRONMENT, "production")()
