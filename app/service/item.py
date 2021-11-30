#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kaiqiang.zhao

from sqlalchemy.orm import Session
from app.curd.item import ItemModelCurd
from app.schema import user as schema


class ItemService:
    def __init__(self):
        self.item_model_curd = ItemModelCurd()

    def get_items(self, db: Session, skip: int = 0, limit: int = 100):
        return self.item_model_curd.get_items(db, skip, limit)

    def create_user_item(self, db: Session, item: schema.ItemCreate, user_id: int):
        return self.item_model_curd.create_user_item(db, item, user_id)
