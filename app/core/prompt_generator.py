from pandas import DataFrame
from app.utils.constants import STATIC_PROMPT


def generar_prompt(volumen_por_negocio: DataFrame):
    
    prompt = ""

    for tipo_negocio, grupo in volumen_por_negocio.groupby("tipo_negocio"):
        prompt += f"Para el rubro '{tipo_negocio}':\n"
        for _, row in grupo.iterrows():
            prompt += f"- Producto: {row['nombre']}, Cantidad total solicitada: {row['cantidad_solicitada']}, Equivalente a {row['cantidad_solicitada'] * row['unidad_producto']}{row['unidad_textual']}.\n"
        prompt += "\n"

    prompt += "Proporciona estrategias específicas para cada tipo de negocio para optimizar sus compras y mejorar sus márgenes de ganancia."
    prompt += STATIC_PROMPT
    return prompt