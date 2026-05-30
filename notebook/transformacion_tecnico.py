import pandas as pd
import os

def transformar_datos_tecnicos(datos):
    df = pd.DataFrame(datos)
    os.makedirs("data", exist_ok=True)

    # ── PROTECCIÓN CONTRA NULOS (fillna) ──
    if "idTecnico" in df.columns:
        df["idTecnico"] = df["idTecnico"].fillna(0)
    if "nombre" in df.columns:
        df["nombre"] = df["nombre"].fillna("")
    if "email" in df.columns:
        df["email"] = df["email"].fillna("")

    # 1. Técnicos activos (id>0) agrupados por descripción/especialidad
    filtro = df.query("idTecnico>0")
    agrupacion = filtro.groupby("descripcion")["idTecnico"].count().reset_index(name="conteo")

    # 2. Técnicos con id menor a 5 agrupados por nombre
    filtro2 = df.query("idTecnico<5")
    agrupacion2 = filtro2.groupby("nombre")["idTecnico"].count().reset_index(name="conteo")

    # 3. Técnicos agrupados por email (conteo sencillo)
    filtro3 = df.query("idTecnico>0")
    agrupacion3 = filtro3.groupby("email")["idTecnico"].count().reset_index(name="conteo")

    # 4. Conteo general de técnicos por nombre
    filtro4 = df.query("idTecnico>0")
    agrupacion4 = filtro4.groupby("nombre")["idTecnico"].count().reset_index(name="conteo")

    # 5. Técnicos con id mayor a 2 agrupados por descripción
    filtro5 = df.query("idTecnico>2")
    agrupacion5 = filtro5.groupby("descripcion")["idTecnico"].count().reset_index(name="conteo")

    # ── EXPORTAR A JSON ──
    agrupacion.to_json("data/tecnicos_activos_descripcion.json", orient="records", indent=4)
    agrupacion2.to_json("data/tecnicos_nuevos_nombre.json", orient="records", indent=4)
    agrupacion3.to_json("data/tecnicos_general_email.json", orient="records", indent=4)
    agrupacion4.to_json("data/tecnicos_general_nombre.json", orient="records", indent=4)
    agrupacion5.to_json("data/tecnicos_antiguos_descripcion.json", orient="records", indent=4)

    transformacion_resumen = {
        "tecnicosActivosPorDescripcion": agrupacion,
        "tecnicosNuevosPorNombre": agrupacion2,
        "conteoGeneralPorEmail": agrupacion3,
        "conteoGeneralPorNombre": agrupacion4,
        "tecnicosAntiguosPorDescripcion": agrupacion5
    }

    return transformacion_resumen
