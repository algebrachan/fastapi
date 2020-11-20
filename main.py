from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from routers.base import base_router

app = FastAPI()

# 跨域 CORS问题解决
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(base_router)



@app.get("/")
def read_root():
    return {"message": "ok"}


if __name__ == '__main__':
    uvicorn.run(app='main:app', host="127.0.0.1",
                port=8001, reload=True, debug=True)
