import pandas as pd
import random
from app.utils.seed import set_seed

def generar_pedidos(num_pedidos=100):
    set_seed(42)  # Por reproducibilidad
    return pd.DataFrame({
        "socio_id": [random.randint(1, 20) for _ in range(num_pedidos)],
        "producto_id": [random.randint(1, 20) for _ in range(num_pedidos)],
        "cantidad_solicitada": [random.randint(1, 50) for _ in range(num_pedidos)]
    })
