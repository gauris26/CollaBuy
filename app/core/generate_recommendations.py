import pandas as pd
from core.json_processor import procesar_respuesta_json
from core.negocio_analisis import agrupar_por_negocio
from core.prompt_generator import generar_prompt
from data.productos import productos
from data.socios import socios
from utils.openai_client import generate_json

def generate_recommendations(socios_seleccionados: pd.DataFrame, selected_rubros: pd.DataFrame, resultado_pedidos: pd.DataFrame):
    try:
        # Verifica si los datos necesarios están presentes
        if socios_seleccionados.empty or selected_rubros.empty or resultado_pedidos.empty:
            raise Exception("Missing required data (socios_seleccionados, selected_rubros, or resultado_pedidos).")
        
        # Filtrar los socios seleccionados según el rubro
        socios_seleccionados = socios_seleccionados[socios_seleccionados['rubro_id'].isin(selected_rubros['id'])]

        # Procesar los pedidos y agrupar por rubros y socios
        volumen_por_negocio = agrupar_por_negocio(resultado_pedidos, socios_seleccionados, productos)

        # Generar el prompt dinámicamente
        prompt = generar_prompt(volumen_por_negocio, productos)

        # Enviar el prompt a OpenAI y obtener la respuesta
        raw_response = generate_json(prompt)

        # Validar y procesar la respuesta JSON
        validated_response = procesar_respuesta_json(raw_response)

        if validated_response:
            return validated_response.model_dump()
        else:
            raise Exception("Invalid JSON response from Llama.")

    except Exception as e:
        raise e
        #raise Exception(f"Error generating recommendations: {str(e)}")
