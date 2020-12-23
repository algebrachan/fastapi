from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from routers.base_router import base_router
from routers.dv_router import dv_router
import config
import utils.log
import tick
app = FastAPI(title='智慧大屏api', description='系统后端restful api')

# 跨域 CORS问题解决
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# app.include_router(base_router)
# 可以加前缀 prefix
app.include_router(dv_router, prefix="/api")



@app.get("/")
def read_root():
    return {"message": "ok"}


# 调试服务
if __name__ == '__main__':
    uvicorn.run(app='main:app', host="0.0.0.0",
                port=8001, reload=True, debug=True)
