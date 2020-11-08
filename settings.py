#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kaiqiang.zhao

import os
from configparser import ConfigParser

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
ENV_CONFIG_PATH = "config/dev.ini"

_config = ConfigParser()
_config.read(os.path.join(BASE_DIR, ENV_CONFIG_PATH), encoding="utf-8")

DATABASE_URL = _config.get("database", "url")

PROJECT_NAME = _config.get("project", "name")
PROJECT_DEBUG = _config.get("project", "debug")
PROJECT_VERSION = _config.get("project", "version")
API_PREFIX = "/api"