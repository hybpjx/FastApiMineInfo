# 导入FastAPI模块
from fastapi import FastAPI, APIRouter

# 创建app实例
from sqlalchemy import desc
from starlette.responses import JSONResponse
from tutorial.database import session
from tutorial.models import MineInfo
from tutorial.schemas import CreatMineInfo

router = APIRouter()
test_router = APIRouter()

# 添加单个
@router.post("/addinfo")
async def AddInfo(addinfo: CreatMineInfo):
    try:
        # 添加数据
        dataInfo = MineInfo(id=addinfo.id,
                            applicator=addinfo.applicator,
                            project_name=addinfo.project_name,
                            produce_type=addinfo.produce_type,
                            examining=addinfo.examining,
                            get_type=addinfo.get_type,
                            main_mine=addinfo.main_mine,
                           create_time=addinfo.create_time)
        session.add(dataInfo)
        session.commit()
        session.close()
    except ArithmeticError:
        return {"code": "0002", "message": "数据库异常"}
    return {"code": "0000", "message": "添加成功"}


## 查询所有
@router.get("/getinfo/")
async def GetInfo():
    # 创建Query查询，filter是where条件，调用one返回唯一行，调用all则是返回所有行
    try:
        data = session.query(MineInfo).order_by(desc(MineInfo.create_time)).limit(100).all()
        session.close()
        # user1 是一个列表，内部元素为字典
        return data
    except ArithmeticError:
        return {"code": "0002", "message": "数据库异常"}


# 注意，视图这里使用router来声明请求方式&URI
@router.get('/info')
def user_list():
    # vue的响应数据
    items = [
        {'id': '1', 'name': 'phyger'},
        {'id': '2', 'name': 'fly'},
        {'id': '3', 'name': 'enheng'},
    ]
    return JSONResponse(content=items)


