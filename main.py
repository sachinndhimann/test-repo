from fastapi import FastAPI
from app.api import router as api_router
from app.database import database, engine, metadata

metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api_router, prefix="/api")

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
