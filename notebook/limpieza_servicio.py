import pandas as pd

def limpiar_servicios(df):
    df_limpio = df.copy()

    # 1. limpiar texto
    columnas_texto = ["nombre", "descripcion"]
    for col in columnas_texto:
        df_limpio[col] = df_limpio[col].astype("string").str.strip()

    # 2. valores válidos
    servicios_validos = [
        "Mantenimiento",
        "Diagnostico",
        "Reparacion"
    ]

    df_limpio["nombre"] = df_limpio["nombre"].where(
        df_limpio["nombre"].isin(servicios_validos),
        pd.NA
    )

    # 3. numéricos
    df_limpio["id_servicio"] = pd.to_numeric(df_limpio["id_servicio"])
    df_limpio["precio_base"] = pd.to_numeric(df_limpio["precio_base"])

    # 4. eliminar nulos críticos
    df_limpio = df_limpio.dropna(
        subset=["id_servicio", "nombre", "precio_base"]
    )

    # 5. reglas de negocio
    df_limpio = df_limpio[df_limpio["id_servicio"] > 0]
    df_limpio = df_limpio[df_limpio["precio_base"] > 0]

    # 6. duplicados
    df_limpio = df_limpio.drop_duplicates()

    return df_limpio