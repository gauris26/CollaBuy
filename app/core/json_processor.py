from pydantic import ValidationError
from models.llama_response import ResponseModel

# Función para validar y convertir la respuesta en un modelo JSON
def procesar_respuesta_json(respuesta: str):
    try:
        # Validar la respuesta generada con el modelo de Pydantic
        response_data = ResponseModel.model_validate_json(respuesta)
        return response_data
    except ValidationError as e:
        print(f"Error de validación: {e}")
        return None