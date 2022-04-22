from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.templating import Jinja2Templates
from .curd import get_mine_info
from tutorial.database import SessionLocal,engine
from .schemas import MineInfoBase

home_router = APIRouter()

templates = Jinja2Templates(directory="templates")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@home_router.get('/')
async def index():
    return "this is a page"


# 注意，视图这里使用router来声明请求方式&uri
@home_router.get('/info',response_model=MineInfoBase)
async def user_list(db: Session = Depends(get_db)):
    items = get_mine_info(db)
    return items


@home_router.get('/')
async def welcome():
    return "这里是测试路由"


@home_router.get('/check')
def home(request: Request):
    return templates.TemplateResponse('home.html', context={'request': request, })
