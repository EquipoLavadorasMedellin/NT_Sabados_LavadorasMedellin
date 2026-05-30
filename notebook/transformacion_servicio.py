import pandas as pd
import os

def transformar_datos_servicios(datos):
    df = pd.DataFrame(datos)
    
    # ── NUEVO: Crear carpeta data si no existe para guardar los JSON ──
    os.makedirs("data", exist_ok=True)

    # ── NUEVO: PROTECCIÓN CONTRA NULOS (fillna) ──
    # Si viene nulo desde la base de datos, lo reemplazamos por 0 o ""
    # para que .query() no lance un error (RIESGO 1 Y 2 resueltos).
    if "precioBase" in df.columns:
        df["precioBase"] = df["precioBase"].fillna(0)
    if "nombre" in df.columns:
        df["nombre"] = df["nombre"].fillna("")
    if "idServicio" in df.columns:
        df["idServicio"] = df["idServicio"].fillna(0)

    # 1. Conteo de mantenimientos por nombre
    filtro = df.query("nombre=='Mantenimiento'")
    agrupacion = filtro.groupby("nombre")["idServicio"].count().reset_index(name="conteo")

    # 2. Sumatoria de costo para servicios caros
    filtro2 = df.query("precioBase>=100000")
    agrupacion2 = filtro2.groupby("nombre")["precioBase"].sum().reset_index(name="sumatoria")

    # 3. Promedio de precios por servicio
    filtro3 = df.query("precioBase>0")
    agrupacion3 = filtro3.groupby("nombre")["precioBase"].mean().reset_index(name="promedio")

    # 4. Conteo de tipos de reparación por descripción
    filtro4 = df.query("nombre=='Reparacion'")
    agrupacion4 = filtro4.groupby("descripcion")["idServicio"].count().reset_index(name="conteo")

    # 5. Conteo general de servicios por nombre
    filtro5 = df.query("idServicio>0")
    agrupacion5 = filtro5.groupby("nombre")["idServicio"].count().reset_index(name="conteo")

    # ── NUEVO: EXPORTAR A JSON SEGÚN REQUERIMIENTO DE LA GUÍA ──
    agrupacion.to_json("data/servicios_conteo_mantenimiento.json", orient="records", indent=4)
    agrupacion2.to_json("data/servicios_sumatoria_caros.json", orient="records", indent=4)
    agrupacion3.to_json("data/servicios_promedio_precios.json", orient="records", indent=4)
    agrupacion4.to_json("data/servicios_conteo_reparaciones.json", orient="records", indent=4)
    agrupacion5.to_json("data/servicios_conteo_general.json", orient="records", indent=4)

    transformacion_resumen = {
        "conteoMantenimiento": agrupacion,
        "sumatoriaServiciosCaros": agrupacion2,
        "promedioPreciosPorServicio": agrupacion3,
        "conteoReparaciones": agrupacion4,
        "conteoGeneralServicios": agrupacion5
    }

    return transformacion_resumen
