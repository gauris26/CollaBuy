from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def health_check():
    """
    Basic health check endpoint.
    """
    return {"status": "ok", "message": "API is running"}
