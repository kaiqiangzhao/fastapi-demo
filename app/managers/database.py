# -*- coding: utf-8 -*-
# __author__ = "kaiqiangzhao"

from __future__ import unicode_literals, print_function, division
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings import DATABASE_URL

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Model = declarative_base()
Model.metadata.create_all(bind=engine)
