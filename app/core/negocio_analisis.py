from pandas import DataFrame

def agrupar_por_negocio(pedidos: DataFrame, socios: DataFrame, productos: DataFrame,):
    pedidos_con_negocio = pedidos.merge(socios, on="socio_id", how="left")
    volumen_por_negocio = pedidos_con_negocio.groupby(["tipo_negocio", "producto_id"])["cantidad_solicitada"].sum().reset_index()
    return volumen_por_negocio.merge(productos, left_on="producto_id", right_on="id")