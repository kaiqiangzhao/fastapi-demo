#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kaiqiang.zhao

from sqlalchemy.orm import Session
from app.model.user import User
from app.schema import user as schema


class UserModelCurd:
    def __init__(self):
        self.UserModel = User

    def get_user(self, db: Session, user_id: int):
        return db.query(self.UserModel).filter(User.id == user_id).first()

    def get_user_by_email(self, db: Session, email: str):
        return db.query(self.UserModel).filter(User.email == email).first()

    def get_users(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(self.UserModel).offset(skip).limit(limit).all()

    def create_user(self, db: Session, user: schema.UserCreate):
        fake_hashed_password = user.password + "notreallyhashed"
        db_user = self.UserModel(email=user.email, hashed_password=fake_hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
