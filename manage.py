#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kaiqiang.zhao

import uvicorn
from config import config
from app.main import app


if __name__ == '__main__':
    uvicorn.run(app, host=config.HOST, port=config.PORT)
