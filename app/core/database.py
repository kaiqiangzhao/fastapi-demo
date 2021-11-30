#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kaiqiang.zhao

from sqlalchemy import Column, Integer, DateTime
from datetime import datetime
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:

    def __init__(self, *args, **kwargs):
        super(Base, self).__init__(*args, **kwargs)

    @classmethod
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)
    create_at = Column(DateTime, default=datetime.now)