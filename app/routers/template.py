#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kaiqiang.zhao

from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse
from app.core.template import template

router = APIRouter()


@router.get("/{username}", response_class=HTMLResponse)
async def read_item(request: Request):
    return template.TemplateResponse("index.html", {"request": request})
