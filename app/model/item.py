#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kaiqiang.zhao

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base


class Item(Base):
    __tablename__ = "item"

    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("user.id"))

    owner = relationship("User", back_populates="items")
