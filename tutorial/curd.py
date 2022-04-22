"""
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 #
# @Time    : 2022/4/22 13:58
# @Author  : zicliang
# @Email   : hybpjx@163.com
# @File    : curd.py
# @Software: PyCharm
"""
#curd.py
from sqlalchemy.orm import Session

from . import models, schemas

def get_mine_info(db: Session):
    return db.query(models.MineInfoModel).all()


