#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kaiqiang.zhao

from fastapi import APIRouter
from app.router import user, template, item
from app.const.api import API_PREFIX

router = APIRouter()
router.include_router(user.router, prefix=API_PREFIX)
router.include_router(item.router, prefix=API_PREFIX)
router.include_router(template.router, prefix="")