#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kaiqiang.zhao
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base


class User(Base):
    __tablename__ = "user"

    email = Column(String, unique=True, index=True)
    hashed_password = Column(String(length=256))
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")

