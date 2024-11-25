import streamlit as st
import pandas as pd
from core.generate_recommendations import generate_recommendations
from data.productos import productos
from data.socios import socios
from data.rubros import rubros

# Mapeo rubro_id a nombres de rubros
rubro_mapping = dict(zip(rubros["id"], rubros["nombre_rubro"]))

# Inicializar estado de la sesión
if "pedidos" not in st.session_state:
    st.session_state.pedidos = []
if "selected_rubros" not in st.session_state:
    st.session_state.selected_rubros = []
if "selected_socio" not in st.session_state:
    st.session_state.selected_socio = None
if "confirmar_pedidos" not in st.session_state:
    st.session_state.confirmar_pedidos = False  # Guardar estado del botón

# Función para mostrar productos y procesar pedidos
def mostrar_productos(selected_rubros):
    productos_filtrados = productos[productos["rubro_id"].isin(selected_rubros)] if selected_rubros else pd.DataFrame()

    if not productos_filtrados.empty:
        st.write("### Productos disponibles:")
        for _, prod in productos_filtrados.iterrows():
            col1, col2 = st.columns([2, 1])
            with col1:
                st.write(f"- **{prod['nombre']}**: ${prod['precio_unitario']} por {prod['unidad_producto']}{prod['unidad_textual']}")
            with col2:
                # Establecemos una clave única por producto para controlar su estado
                key = f"cantidad_{prod['id']}"
                cantidad = st.session_state.get(key, 0)  # Obtener cantidad desde session_state, o 0 si no existe
                cantidad = st.number_input(
                    f"Cantidad para {prod['nombre']}",
                    min_value=0, step=1,
                    key=key,
                    value=cantidad
                )
                
                # Si la cantidad es mayor que 0, agregamos o actualizamos el producto en los pedidos
                if cantidad > 0:
                    # Verificamos si el producto ya existe en los pedidos
                    existing_pedido = next((p for p in st.session_state.pedidos if p["producto_id"] == prod["id"]), None)
                    if existing_pedido:
                        # Si existe, actualizamos la cantidad
                        existing_pedido["cantidad_solicitada"] = cantidad
                    else:
                        # Si no existe, lo agregamos como nuevo pedido
                        pedido = {"producto_id": prod["id"], "nombre": prod["nombre"], "cantidad_solicitada": cantidad}
                        st.session_state.pedidos.append(pedido)

# Función para parsear y mostrar el JSON
def mostrar_recomendaciones(json_data):
    # Mostrar recomendaciones generales
    if "recomendaciones_generales" in json_data:
        st.write("### Recomendaciones Generales:")
        for recomendacion in json_data["recomendaciones_generales"]:
            st.write(f"- {recomendacion}")

    # Mostrar recomendaciones por rubro
    if "rubros" in json_data:
        for rubro in json_data["rubros"]:
            st.write(f"### Rubro: {rubro['nombre_rubro']}")
            st.write("**Productos recomendados:**")
            
            # Mostrar productos dentro de cada rubro
            for producto in rubro["productos"]:
                st.write(f"#### Producto: {producto['nombre_producto']}")
                st.write(f"  - **Demanda:** {producto['demanda']}")
                st.write(f"  - **Acción sugerida:** {producto['accion_sugerida']}")
                st.write(f"  - **Motivo:** {producto['motivo']}")
                
                # Mostrar recomendaciones específicas para cada producto
                if "recomendaciones" in producto:
                    st.write("  - **Recomendaciones:**")
                    for recomendacion in producto["recomendaciones"]:
                        st.write(f"    - {recomendacion}")

# Mostrar el formulario para seleccionar rubros
st.title("CollaBuy: Selección de Rubros y Productos")
selected_rubros = st.multiselect(
    "Selecciona uno o más rubros:",
    options=rubros["id"],
    default=st.session_state.selected_rubros,
    format_func=lambda x: rubro_mapping[x]
)

# Guardar los rubros seleccionados en el estado de la sesión
st.session_state.selected_rubros = selected_rubros

# Crear DataFrame para selected_rubros
df_selected_rubros = rubros[rubros["id"].isin(selected_rubros)][["id", "nombre_rubro"]]

# Mostrar productos basados en los rubros seleccionados
mostrar_productos(selected_rubros)

# Resumen de Pedidos
if st.session_state.pedidos:
    st.write("### Resumen de Pedidos:")
    for pedido in st.session_state.pedidos:
        st.write(f"- Producto: **{pedido['nombre']}**, Cantidad: **{pedido['cantidad_solicitada']}**")
else:
    st.write("No se han realizado pedidos aún.")

# Confirmar pedidos y seleccionar socio
if not st.session_state.confirmar_pedidos:
    if st.button("Confirmar Pedidos"):
        st.session_state.confirmar_pedidos = True

# Si el botón ha sido presionado, procesar la confirmación de pedidos
if st.session_state.confirmar_pedidos:
    if st.session_state.pedidos:
        # Filtrar socios según los rubros seleccionados
        socios_filtrados = socios[socios["rubro_id"].isin(selected_rubros)]

        if not socios_filtrados.empty:

            rubros_renombrados = rubros[["id", "nombre_rubro"]].rename(columns={"id": "rubro_id"})
            
            # Agregar el nombre del rubro a los socios filtrados
            socios_filtrados = socios_filtrados.merge(rubros_renombrados, how="left", on="rubro_id")
            
            st.write("### Selecciona un Socio:")
            
            selected_socio = st.selectbox(
                "Selecciona un socio relacionado con los rubros seleccionados:",
                options=socios_filtrados["socio_id"],
                format_func=lambda x: socios[socios["socio_id"] == x]["nombre"].values[0],
                key="select_socio",
                index=None if st.session_state.selected_socio is None else
                    list(socios_filtrados["socio_id"]).index(st.session_state.selected_socio)
            )

            st.session_state.selected_socio = selected_socio

            # Mostrar nombre del socio seleccionado
            if selected_socio is not None:
                socio_seleccionado = socios[socios["socio_id"] == selected_socio]
                if not socio_seleccionado.empty:
                    st.write(f"Has seleccionado al socio: **{socio_seleccionado['nombre'].values[0]}**")
                else:
                    st.write("El socio seleccionado no es válido.")
        else:
            st.write("No hay socios disponibles para los rubros seleccionados.")
        
        if selected_socio and st.session_state.pedidos:
            pedidos_df = pd.DataFrame(st.session_state.pedidos)
            pedidos_df['socio_id'] = selected_socio  # Agregar el socio_id al DataFrame de pedidos

            recomendaciones = generate_recommendations(
                socios_seleccionados=socios_filtrados.rename(columns={"id": "socio_id"}),
                selected_rubros=df_selected_rubros,
                resultado_pedidos=pedidos_df
            )
            st.write("### Recomendaciones Basadas en tus Pedidos:")
            st.write(recomendaciones)

            mostrar_recomendaciones(recomendaciones)
    else:
        st.write("No hay pedidos para confirmar.")
else:
    st.write("Selecciona rubros, productos y confirma los pedidos.")
