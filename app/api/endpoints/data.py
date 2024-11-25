from fastapi import APIRouter
from app.data.socios import socios
from app.data.productos import productos

router = APIRouter()

@router.get("/socios")
async def obtener_socios():
    """
    Obtener la lista de socios con su información.
    """
    return socios.to_dict(orient="records")

@router.get("/productos")
async def obtener_productos():
    """
    Obtener la lista de productos con su información.
    """
    return productos.to_dict(orient="records")
