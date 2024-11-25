import pandas as pd

# DataFrame de socios con rubro_id
socios = pd.DataFrame({
    "socio_id": range(1, 21),  # 20 socios
    "nombre": [
        "Café Express", "Supermercado Verde", "La Bodega", "Tech World", "Peluquería Glam",
        "Bar La Esquina", "Spa Relax", "Distribuidora Alimentos", "Farmacia Vida", "Licorería Premium",
        "Restaurante Delicias", "Panadería Doña Rosa", "Tienda EcoFriendly", "Ferretería El Tornillo",
        "Librería Central", "MiniMarket La Esquina", "Clínica Dental Pro", "Cine Star", 
        "Parque de Diversiones", "Tienda de Mascotas"
    ],
    "rubro_id": [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20
    ]
})