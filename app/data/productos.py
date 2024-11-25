import pandas as pd

# Universo de productos variados
productos = pd.DataFrame({
    "id": range(1, 21),
    "nombre": [
        "Café en grano 1kg", "Azúcar 5kg", "Leche en polvo 1kg", "Shampoo 500ml",
        "Aceite para masaje 250ml", "Whisky 12 años 750ml", "Cerveza artesanal 500ml",
        "Vino tinto botella 750ml", "Queso cheddar 1kg", "Smartphone 128GB",
        "Laptop 15'' 512GB SSD", "Tablet 64GB", "Arroz 5kg", "Frijoles 2kg",
        "Pasta 1kg", "Crema facial 100ml", "Secador de cabello", "Cepillo de pelo",
        "Enjuague bucal 1L", "Tequila blanco 750ml"
    ],
    "precio_unitario": [
        15.00, 8.00, 12.00, 5.50, 10.00, 45.00, 3.50, 18.00, 7.50, 300.00,
        800.00, 200.00, 7.00, 6.50, 3.00, 20.00, 50.00, 15.00, 8.00, 35.00
    ],
    "unidad_producto": [
        1, 5, 1, 0.5, 0.25, 0.75, 0.5, 0.75, 1, 1, 1, 1, 5, 2, 1, 0.1, 1, 1, 1, 0.75
    ],
    "unidad_textual": [
        "kg", "kg", "kg", "ml", "ml", "ml", "ml", "ml", "kg", "u",
        "u", "u", "kg", "kg", "kg", "ml", "u", "u", "L", "ml"
    ],
    "rubro_id": [
        1, 2, 2, 4, 7, 10, 10, 10, 2, 4, 
        4, 4, 2, 2, 2, 7, 5, 5, 8, 10
    ]  # Relación de producto con el rubro
})