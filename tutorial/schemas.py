"""
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 #
# @Time    : 2022/4/22 13:59
# @Author  : zicliang
# @Email   : hybpjx@163.com
# @File    : schemas.py
# @Software: PyCharm
"""
from typing import List, Optional
from pydantic import BaseModel



class MineInfoBase(BaseModel):
    id:int
    applicator: str
    project_name: str
    produce_type: str
    examining: str
    get_type: str
    main_mine: str
    create_time: str

    class Config:
        #  orm_mode 会告诉 Pydantic 模型读取数据，即使它不是字典，而是 ORM 模型(或任何其他具有属性的任意对象)
        orm_mode = True



