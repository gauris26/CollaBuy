from fastapi import APIRouter
from app.api.endpoints import llama_results, health

api_router = APIRouter()

# Register endpoints
api_router.include_router(llama_results.router, prefix="/llama", tags=["Llama"])
api_router.include_router(health.router, prefix="/health", tags=["Health"])
