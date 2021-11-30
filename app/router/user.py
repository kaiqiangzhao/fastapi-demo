#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kaiqiang.zhao
from typing import List

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from app.schema import user as user_schemas
from app.service.user import UserService
from app.service.item import ItemService
from app.core.session import get_db

router = APIRouter()


@router.post("/users/", response_model=user_schemas.User)
def create_user(user: user_schemas.UserCreate, db: Session = Depends(get_db)):
    user_service = UserService()
    db_user = user_service.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_service.create_user(db=db, user=user)


@router.get("/users/", response_model=List[user_schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    user_service = UserService()
    users = user_service.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=user_schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user_service = UserService()
    db_user = user_service.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


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
