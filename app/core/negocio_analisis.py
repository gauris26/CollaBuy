from pandas import DataFrame

def agrupar_por_negocio(resultado_pedidos: DataFrame, socios: DataFrame, productos: DataFrame):
       
    # Unir los pedidos con los socios para obtener el tipo de negocio
    pedidos_con_negocio = resultado_pedidos.merge(socios[['socio_id', 'nombre_rubro']], on="socio_id", how="left")
    
    # Agrupar por tipo de negocio y producto, sumando las cantidades solicitadas
    volumen_por_negocio = pedidos_con_negocio.groupby(["nombre_rubro", "producto_id"])["cantidad_solicitada"].sum().reset_index()

    # Unir el volumen por negocio con los productos para obtener detalles del producto
    resultado = volumen_por_negocio.merge(productos[['id', 'nombre']], left_on="producto_id", right_on="id", how="left")
    
    # Devolver solo las columnas relevantes
    return resultado[['producto_id','nombre_rubro', 'nombre', 'cantidad_solicitada']]
