from fastapi import FastAPI
app = FastAPI()
app.include_router(todo.router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", reload=True)