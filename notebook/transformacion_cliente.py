import pandas as pd
import os

def transformar_datos_clientes(datos):
    df = pd.DataFrame(datos)
    os.makedirs("data", exist_ok=True)

    # ── PROTECCIÓN CONTRA NULOS (fillna) ──
    if "idCliente" in df.columns:
        df["idCliente"] = df["idCliente"].fillna(0)
    if "nombre" in df.columns:
        df["nombre"] = df["nombre"].fillna("")

    # 1. Clientes con ID mayor a 5 agrupados por dirección
    filtro = df.query("idCliente>5")
    agrupacion = filtro.groupby("direccion")["idCliente"].count().reset_index(name="conteo")

    # 2. Clientes con ID menor o igual a 5 agrupados por nombre
    filtro2 = df.query("idCliente<=5")
    agrupacion2 = filtro2.groupby("nombre")["idCliente"].count().reset_index(name="conteo")

    # 3. Conteo general de clientes por dirección
    filtro3 = df.query("idCliente>0")
    agrupacion3 = filtro3.groupby("direccion")["idCliente"].count().reset_index(name="conteo")

    # 4. Conteo general de clientes por nombre
    filtro4 = df.query("idCliente>0")
    agrupacion4 = filtro4.groupby("nombre")["idCliente"].count().reset_index(name="conteo")

    # 5. Conteo general de clientes por teléfono
    filtro5 = df.query("idCliente>0")
    agrupacion5 = filtro5.groupby("telefono")["idCliente"].count().reset_index(name="conteo")

    # ── EXPORTAR A JSON ──
    agrupacion.to_json("data/clientes_mayores_5.json", orient="records", indent=4)
    agrupacion2.to_json("data/clientes_menores_5.json", orient="records", indent=4)
    agrupacion3.to_json("data/clientes_general_direccion.json", orient="records", indent=4)
    agrupacion4.to_json("data/clientes_general_nombre.json", orient="records", indent=4)
    agrupacion5.to_json("data/clientes_general_telefono.json", orient="records", indent=4)

    transformacion_resumen = {
        "clientesMayoresA5PorDireccion": agrupacion,
        "clientesMenoresA5PorNombre": agrupacion2,
        "conteoGeneralPorDireccion": agrupacion3,
        "conteoGeneralPorNombre": agrupacion4,
        "conteoGeneralPorTelefono": agrupacion5
    }

    return transformacion_resumen
