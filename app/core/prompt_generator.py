from pandas import DataFrame
from utils.constants import STATIC_PROMPT

def generar_prompt(volumen_por_negocio: DataFrame, productos: DataFrame):

    prompt = ""

    # Agrupar por tipo de negocio (nombre_rubro) y recorrer cada grupo
    for tipo_negocio, grupo in volumen_por_negocio.groupby("nombre_rubro"):
        prompt += f"Para el rubro '{tipo_negocio}':\n"
        
        # Para cada producto en el grupo, generar la descripción
        for _, row in grupo.iterrows():
            producto_info = productos[productos['id'] == row['producto_id']].iloc[0]
            
            # Obtener el nombre del producto, la cantidad solicitada y la unidad
            nombre_producto = producto_info['nombre']
            cantidad_total = row['cantidad_solicitada']
            cantidad_equivalente = cantidad_total * producto_info['unidad_producto']
            unidad_textual = producto_info['unidad_textual']
            
            prompt += f"- Producto: {nombre_producto}, Cantidad total solicitada: {cantidad_total}, " \
                      f"Equivalente a {cantidad_equivalente}{unidad_textual}.\n"
        
        prompt += "\n"

    prompt += "Proporciona estrategias específicas para cada tipo de negocio para optimizar sus compras y mejorar sus márgenes de ganancia."
    prompt += STATIC_PROMPT
    return prompt