#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kaiqiang.zhao

import uvicorn
from config import config


if __name__ == '__main__':
    reload = False
    if config.DEBUG:
        reload = True
    uvicorn.run("app.main:app", host=config.HOST, port=config.PORT, reload=reload)
