"""
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 #
# @Time    : 2022/4/22 14:02
# @Author  : zicliang
# @Email   : hybpjx@163.com
# @File    : models.py
# @Software: PyCharm
"""
from sqlalchemy import Column, Integer, String
from tutorial.database import Base, engine


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


if __name__ == '__main__':
    Base.metadata.create_all(engine)
