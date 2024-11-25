import pandas as pd

def generar_pedidos(socios_seleccionados: pd.DataFrame, selected_productos: pd.DataFrame, cantidades: dict):
       
    # Filtramos los productos seleccionados en un DataFrame
    productos_seleccionados = selected_productos[selected_productos['id'].isin(cantidades.keys())]

    # Creamos un DataFrame para los pedidos combinando los socios seleccionados con los productos y las cantidades
    pedidos = pd.merge(
        socios_seleccionados[['socio_id']],  # Solo tomamos la columna de socio_id
        productos_seleccionados[['id', 'nombre']],  # Tomamos id y nombre del producto
        how='cross'  # Realizamos un cruce de todos los socios con todos los productos seleccionados
    )

    # Añadimos la cantidad de cada producto a cada pedido
    pedidos['cantidad_solicitada'] = pedidos['id'].map(cantidades)

    # Filtramos los pedidos para que solo se queden aquellos con cantidad solicitada > 0
    pedidos = pedidos[pedidos['cantidad_solicitada'] > 0]

    # Renombramos las columnas para devolver 'producto_id' en vez de 'id'
    pedidos.rename(columns={'id': 'producto_id'}, inplace=True)

    # Regresamos el DataFrame de pedidos
    return pedidos[['socio_id', 'producto_id', 'cantidad_solicitada']]

