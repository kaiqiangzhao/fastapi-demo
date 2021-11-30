#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kaiqiang.zhao

from sqlalchemy.orm import Session
from app.model.item import Item
from app.schema import user as schema


class ItemModelCurd:
    def __init__(self):
        self.ItemModel = Item

    def get_items(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(self.ItemModel).offset(skip).limit(limit).all()

    def create_user_item(self, db: Session, item: schema.ItemCreate, user_id: int):
        db_item = self.ItemModel(**item.dict(), owner_id=user_id)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
