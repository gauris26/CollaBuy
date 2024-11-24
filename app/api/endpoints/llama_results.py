from fastapi import APIRouter, HTTPException
from app.core.negocio_analisis import agrupar_por_negocio
from app.core.prompt_generator import generar_prompt
from app.core.json_processor import procesar_respuesta_json
from app.utils.openai_client import generate_json
from app.data.socios import socios
from app.data.productos import productos
from app.data.pedidos import generar_pedidos

router = APIRouter()

@router.post("/generate")
async def generate_recommendations(num_pedidos: int = 100):
    """
    Generate recommendations based on orders.
    """
    try:
        # Generate example orders
        pedidos = generar_pedidos(num_pedidos)
        
        # Analyze and group data by business type
        volumen_por_negocio = agrupar_por_negocio(pedidos, socios.head(5), productos)
        
        # Generate the prompt dynamically
        prompt = generar_prompt(volumen_por_negocio)
        
        # Send the prompt to OpenAI and get the response
        raw_response = generate_json(prompt)
        
        # Validate and process the response JSON
        validated_response = procesar_respuesta_json(raw_response)
        
        if validated_response:
            return validated_response.dict()
        else:
            raise HTTPException(status_code=400, detail="Invalid JSON response from OpenAI.")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
