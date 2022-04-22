from fastapi import FastAPI
import uvicorn
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

# from tutorial.test import test_router
from tutorial.home import router

app = FastAPI()

# 接下来🔛再请求 test01中的连接地址 就需要带上前缀了  tags代表了api中的标题
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router, prefix="/home",tags=["首页"])


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True, debug=True, workers=1,host="0.0.0.0",port=5000)



# coronavirus
# tutorial