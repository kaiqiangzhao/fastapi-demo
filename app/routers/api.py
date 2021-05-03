#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kaiqiang.zhao

from fastapi import APIRouter
from app.routers import users, template
from app.const.api import API_PREFIX

router = APIRouter()
router.include_router(users.router, prefix=API_PREFIX)
router.include_router(template.router, prefix="")