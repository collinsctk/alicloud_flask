#!/usr/bin/env python3.8
# -*- coding=utf-8 -*-

from sqlalchemy import create_engine, orm
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey

db_username = "qytangdbuser"
db_password = "Cisc0123"
db_dns = "127.0.0.1"
db_name = "qytangdb"

engine = create_engine(f'postgresql+psycopg2://{db_username}:{db_password}@{db_dns}/{db_name}')

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
