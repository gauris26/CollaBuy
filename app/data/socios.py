import pandas as pd

socios = pd.DataFrame({
    "socio_id": range(1, 21),  # 20 socios
    "nombre": [
        "Café Express", "Supermercado Verde", "La Bodega", "Tech World", "Peluquería Glam",
        "Bar La Esquina", "Spa Relax", "Distribuidora Alimentos", "Farmacia Vida", "Licorería Premium",
        "Restaurante Delicias", "Panadería Doña Rosa", "Tienda EcoFriendly", "Ferretería El Tornillo",
        "Librería Central", "MiniMarket La Esquina", "Clínica Dental Pro", "Cine Star", "Parque de Diversiones", "Tienda de Mascotas"
    ],
    "tipo_negocio": [
        "Cafetería", "Supermercado", "Bodega", "Tecnología", "Peluquería", "Bar", "Spa", "Distribuidora", 
        "Farmacia", "Licorería", "Restaurante", "Panadería", "Tienda EcoFriendly", "Ferretería", 
        "Librería", "MiniMarket", "Clínica Dental", "Cine", "Parque de Diversiones", "Mascotas"
    ]
})
socios