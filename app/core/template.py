#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kaiqiang.zhao

from app.core.config import settings
from fastapi.templating import Jinja2Templates

template = Jinja2Templates(directory=settings.web_dir_path)

# 避免和vue语法冲突 修改jinja2模版语法标签
template.env.block_start_string = '(%'  # 修改块开始符号
template.env.block_end_string = '%)'  # 修改块结束符号
template.env.variable_start_string = '(('  # 修改变量开始符号
template.env.variable_end_string = '))'  # 修改变量结束符号
template.env.comment_start_string = '(#'  # 修改注释开始符号
template.env.comment_end_string = '#)'  # 修改注释结束符号
