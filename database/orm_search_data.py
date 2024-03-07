#!/usr/bin/env python3.8
# -*- coding=utf-8 -*-

from sqlalchemy.orm import sessionmaker
from database.orm_create_table import User, engine

Session = sessionmaker(bind=engine)
session = Session()


def get_all_users():
    users = session.query(User).all()
    staff_list = []
    for user in users:
        staff_list.append({
            'username': user.username,
            'phone': user.phone,
            'QQ': user.QQ,
            'email': user.email
        })

    return staff_list


if __name__ == '__main__':
    print(get_all_users())
