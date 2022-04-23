# models.py
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


# 创建表模型

class MineInfo(Base):
    __tablename__ = 'mineinfo'

    id = Column(Integer, primary_key=True, autoincrement=True)
    applicator = Column(String(128))
    project_name = Column(String(255))
    produce_type = Column(String(128))
    examining = Column(String(255))
    get_type = Column(String(128))
    main_mine = Column(String(255))
    create_time = Column(String(128))

    # 构造函数
    def __init__(self, id, applicator, project_name, produce_type, examining, get_type, main_mine, create_time, ):
        self.id = id
        self.applicator = applicator
        self.project_name = project_name
        self.produce_type = produce_type
        self.examining = examining
        self.get_type = get_type
        self.main_mine = main_mine
        self.create_time = create_time

    # 打印形式
    def __str__(self):
        return "id：%s, " \
               "applicator：%s, " \
               "project_name：%s, " \
               "produce_type：%s, " \
               "examining：%s, " \
               "get_type：%s, " \
               "main_mine：%s, " \
               "create_time：%s" \
               % (self.id, self.applicator, self.project_name, self.produce_type, self.examining, self.get_type,
                  self.main_mine, self.create_time,)

    # 定义返回结果
    def to_dict(self):
        return {
            "id": self.id,
            "applicator": self.applicator,
            "project_name": self.project_name,
            "produce_type": self.produce_type,
            "examining": self.examining,
            "get_type": self.get_type,
            "main_mine": self.main_mine,
            "create_time": self.create_time,
        }
