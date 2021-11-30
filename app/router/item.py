#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kaiqiang.zhao
from typing import List

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from app.schema import user as user_schemas
from app.service.item import ItemService
from app.core.session import get_db

router = APIRouter()


@router.post("/users/{user_id}/items/", response_model=user_schemas.Item)
def create_item_for_user(
    user_id: int, item: user_schemas.ItemCreate, db: Session = Depends(get_db)
):
    user_service = ItemService()
    return user_service.create_user_item(db=db, item=item, user_id=user_id)


@router.get("/items/", response_model=List[user_schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    user_service = ItemService()
    items = user_service.get_items(db, skip=skip, limit=limit)
    return items
