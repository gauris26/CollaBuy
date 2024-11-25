import pandas as pd

# Definir los rubros
rubros = pd.DataFrame({
    "id": range(1, 21),  # 20 rubros
    "nombre_rubro": [
        "Cafetería", "Supermercado", "Bodega", "Tecnología", "Peluquería", 
        "Bar", "Spa", "Distribuidora", "Farmacia", "Licorería", 
        "Restaurante", "Panadería", "Tienda EcoFriendly", "Ferretería", 
        "Librería", "MiniMarket", "Clínica Dental", "Cine", 
        "Parque de Diversiones", "Mascotas"
    ]
})