# 导入FastAPI模块
from fastapi import FastAPI, APIRouter

# 创建app实例
from starlette.requests import Request
from starlette.responses import JSONResponse

from starlette.templating import Jinja2Templates
templates = Jinja2Templates('templates')
test_router = APIRouter()


@test_router.get('/')
def welcome():
    return "这里是测试路由"


# 注意，视图这里使用router来声明请求方式&URI
@test_router.get('/info')
def user_list():
    # vue的响应数据
    items = [
        {'id': '1', 'name': 'phyger'},
        {'id': '2', 'name': 'fly'},
        {'id': '3', 'name': 'enheng'},
    ]
    return JSONResponse(content=items)


@test_router.get('/check')
def home(request: Request):
    return templates.TemplateResponse(name='test.html', context={'request': request, })

