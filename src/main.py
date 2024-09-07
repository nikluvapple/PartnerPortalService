from fastapi import FastAPI
from src.modules.api import router as api_router
from mangum import  Mangum

app = FastAPI()

handler = Mangum(app)

@app.get("/")
async def root():
    return {"message": "HealApp API is live"}

app.include_router(api_router, prefix="/api/v1")



