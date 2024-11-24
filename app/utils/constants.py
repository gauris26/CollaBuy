DEFAULT_NUM_PEDIDOS = 100
SYSTEM_PROMPT = "Eres un asistente experto en compras colaborativas. Los socios son quienes se reunen para comprar en volumen a un proveedor, buscando mejores condiciones. Analiza los volúmenes totales solicitados por tipo de negocio y proporciona recomendaciones personalizadas para cada rubro y negociación con los proveedores.Incluye recomendaciones para mejores precios.\n\n"
STATIC_PROMPT = """
Las recomendaciones proporcionadas deben estar estructuradas en el siguiente formato JSON. 
Por favor, devuelve una respuesta en formato JSON "puro" sin ningún delimitador de código como ` ``` `, y sin texto adicional. 
Devuelve un JSON minificado (sin saltos de línea, espacios en blanco o formato adicional). El JSON debe estar en una sola línea.
La respuesta debe ser un JSON estructurado como se muestra a continuación:

{
    "rubros": [
        {
            "nombre_rubro": "Bar",
            "productos": [
                {
                    "nombre_producto": "Café en grano",
                    "demanda": "alta",
                    "accion_sugerida": "comprar en grandes cantidades",
                    "motivo": "reducir el costo unitario",
                    "recomendaciones": [
                    "Comprar grandes cantidades de café en grano para reducir el costo unitario."
                ]
                },
                {
                    "nombre_producto": "Leche en polvo",
                    "demanda": "alta",
                    "accion_sugerida": "comprar en cantidades más pequeñas",
                    "motivo": "evitar sobrepoblación de inventario",
                    "recomendaciones": [
                    "Evitar comprar grandes cantidades de leche en polvo para evitar sobrepoblación de inventario."
                ]
                }
            ]
        },
        {
            "nombre_rubro": "Bodega",
            "productos": [
                {
                    "nombre_producto": "Leche en polvo",
                    "demanda": "alta",
                    "accion_sugerida": "comprar en grandes cantidades",
                    "motivo": "reducir el costo unitario",
                    "recomendaciones": [
                        "Comprar grandes cantidades de leche en polvo para reducir el costo unitario."
                    ]
                },
                {
                    "nombre_producto": "Whisky",
                    "demanda": "baja",
                    "accion_sugerida": "no comprar en grandes cantidades",
                    "motivo": "demanda insuficiente",
                    "recomendaciones": [
                        "Comprar cantidades intermedias de Whisky para equilibrar el costo y la demanda."
                    ]
                }
            ]
        }
    ],
    "recomendaciones_generales": [
    "Los rubros 'Bar' y 'Supermercado' tienen una alta demanda de productos como café en grano y leche en polvo.",
    "Los rubros 'Bodega' y 'Spa' tienen una alta demanda de productos como leche en polvo y aceite para masaje.",
    "Los rubros 'Clínica Dental' y 'Peluquería' tienen una demanda baja de productos como aceite para masaje y shampoo.",
    "Los rubros 'Ferretería' y 'Tienda EcoFriendly' tienen una demanda baja de productos como shampoo y aceite para masaje."
    ]
}

Ahora, analiza el siguiente conjunto de datos y genera una recomendación estructurada en el mismo formato JSON.
"""