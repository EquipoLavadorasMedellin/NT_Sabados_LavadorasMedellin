import pandas as pd
import os

def transformar_datos_reservas(datos):
    df = pd.DataFrame(datos)
    os.makedirs("data", exist_ok=True)

    # ── PROTECCIÓN CONTRA NULOS (fillna) ──
    if "idReserva" in df.columns:
        df["idReserva"] = df["idReserva"].fillna(0)
    if "jornada" in df.columns:
        df["jornada"] = df["jornada"].fillna("")
    if "estado" in df.columns:
        df["estado"] = df["estado"].fillna("")

    # 1. Reservas de la mañana agrupadas por estado
    filtro = df.query("jornada=='MANANA'")
    agrupacion = filtro.groupby("estado")["idReserva"].count().reset_index(name="conteo")

    # 2. Reservas pendientes agrupadas por jornada
    filtro2 = df.query("estado=='Pendiente'")
    agrupacion2 = filtro2.groupby("jornada")["idReserva"].count().reset_index(name="conteo")

    # 3. Reservas de la tarde agrupadas por estado
    filtro3 = df.query("jornada=='TARDE'")
    agrupacion3 = filtro3.groupby("estado")["idReserva"].count().reset_index(name="conteo")

    # 4. Conteo general de reservas por fecha
    filtro4 = df.query("idReserva>0")
    agrupacion4 = filtro4.groupby("fechaReserva")["idReserva"].count().reset_index(name="conteo")

    # 5. Conteo general de reservas por estado
    filtro5 = df.query("idReserva>0")
    agrupacion5 = filtro5.groupby("estado")["idReserva"].count().reset_index(name="conteo")

    # ── EXPORTAR A JSON ──
    agrupacion.to_json("data/reservas_manana.json", orient="records", indent=4)
    agrupacion2.to_json("data/reservas_pendientes.json", orient="records", indent=4)
    agrupacion3.to_json("data/reservas_tarde.json", orient="records", indent=4)
    agrupacion4.to_json("data/reservas_general_fecha.json", orient="records", indent=4)
    agrupacion5.to_json("data/reservas_general_estado.json", orient="records", indent=4)

    transformacion_resumen = {
        "reservasMananaPorEstado": agrupacion,
        "reservasPendientesPorJornada": agrupacion2,
        "reservasTardePorEstado": agrupacion3,
        "conteoGeneralPorFecha": agrupacion4,
        "conteoGeneralPorEstado": agrupacion5
    }

    return transformacion_resumen
