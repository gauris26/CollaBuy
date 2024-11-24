from fastapi import FastAPI
from app.api.router import api_router

app = FastAPI(
    title="CollaBuy: Recommendations API",
    description="API to generate business recommendations using Llama.",
    version="1.0.0"
)

app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": "Welcome to CollaBuy: Business recommendations API!"}