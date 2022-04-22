"""
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 #
# @Time    : 2022/4/22 14:05
# @Author  : zicliang
# @Email   : hybpjx@163.com
# @File    : database.py
# @Software: PyCharm
"""
#database.py
from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

#数据库访问地址
SQLALCHEMY_DATABASE_URL="mysql+pymysql://root:admin*123@192.168.2.59:3306/mineinfo?charset=utf8"

#启动引擎
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
#启动会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#  创建基类, 相当于 django orm中的model.model
Base = declarative_base()

