#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kaiqiang.zhao

from sqlalchemy.orm import Session
from app.curd.user import UserModelCurd
from app.schema import user as schema


class UserService:
    def __init__(self):
        self.user_model_curd = UserModelCurd()

    def get_user(self, db: Session, user_id: int):
        return self.user_model_curd.get_user(db, user_id)

    def get_user_by_email(self, db: Session, email: str):
        return self.user_model_curd.get_user_by_email(db, email)

    def get_users(self, db: Session, skip: int = 0, limit: int = 100):
        return self.user_model_curd.get_users(db, skip, limit)

    def create_user(self, db: Session, user: schema.UserCreate):
        return self.user_model_curd.create_user(db, user)
