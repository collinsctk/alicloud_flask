#!/usr/bin/env python3.8
# -*- coding=utf-8 -*-
from sqlalchemy.orm import sessionmaker
from database.orm_create_table import User, engine

Session = sessionmaker(bind=engine)
session = Session()

user_db = [
    {'username': '秦柯', 'phone': '13911116666', 'QQ': 605658506, 'email': 'collinsctk@qytang.com'},
    {'username': '周亚军', 'phone': '13988886666', 'QQ': 888999, 'email': 'ender@qytang.com'}
]


for user in user_db:
    session.add(User(**user))
    session.commit()
