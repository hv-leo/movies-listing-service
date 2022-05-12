import uvicorn
from fastapi import FastAPI
from app.routes import router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to the movies recomendation system!"}

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', log_level="info")
    print("running")