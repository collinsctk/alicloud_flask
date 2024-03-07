#!/usr/bin/env python3.8
# -*- coding=utf-8 -*-

from sqlalchemy import create_engine, orm
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey


engine = create_engine('postgresql+psycopg2://qytang:Cisc0123@pgm-2zetnw1u261948m7.pg.rds.aliyuncs.com/qytangdb')

Base = orm.declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(64), nullable=False, index=True)
    phone = Column(String(64), nullable=False)
    QQ = Column(String(64), nullable=True)
    email = Column(String(64), nullable=False, index=True)

    def __repr__(self):
        return f"{self.__class__.__name__}(username: {self.username} | email: {self.email})"


if __name__ == '__main__':
    Base.metadata.create_all(engine, checkfirst=True)
