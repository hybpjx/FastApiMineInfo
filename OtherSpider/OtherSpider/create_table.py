"""
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 #
# @Time    : 2022/4/22 13:33
# @Author  : zicliang
# @Email   : hybpjx@163.com
# @File    : create_table.py
# @Software: PyCharm
"""
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine(
    "mysql+pymysql://root:admin*123@192.168.2.59:3306/mineinfo?charset=utf8",
    encoding='latin1', echo=True)


# 2. 创建基类, 相当于 django orm中的model.model


Base = declarative_base()

# 创建表模型

class MineInfoModel(Base):
    __tablename__ = 'mineinfo'

    id = Column(Integer, primary_key=True, autoincrement=True)
    applicator = Column(String(128))
    project_name = Column(String(255))
    produce_type = Column(String(128))
    examining = Column(String(255))
    get_type = Column(String(128))
    main_mine = Column(String(255))
    create_time = Column(String(128))

    def __repr__(self):
        return self.project_name


Base.metadata.create_all(engine)

