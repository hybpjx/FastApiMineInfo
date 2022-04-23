### 添加数据

from pydantic import BaseModel


# 定义数据模型
class CreatMineInfo(BaseModel):
    id: int
    applicator: str
    project_name: str
    produce_type: str
    examining: str
    get_type: str
    main_mine: str
    create_time: str

    def __str__(self):
        return "id：%s, applicator：%s, project_name：%s, produce_type：%s, examining：%s, get_type：%s, main_mine：%s, create_time：%s" \
               % (self.id,self.applicator,self.project_name,self.produce_type,self.examining,self.get_type,self.main_mine,self.create_time,)