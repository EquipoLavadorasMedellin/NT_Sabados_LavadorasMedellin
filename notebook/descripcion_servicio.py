import pandas as pd

def describir_servicios(df_limpio):
    print(f"numero de filas: {df_limpio.shape[0]}")
    print(f"numero de columnas: {df_limpio.shape[1]}")
    print(f"columnas disponibles: {list(df_limpio.columns)}")

    # estadísticas numéricas
    print("\n Estadísticas:")
    print(df_limpio[["id_servicio", "precio_base"]].describe())

    # valores categóricos
    print("\n Frecuencia de servicios:")
    print(df_limpio["nombre"].value_counts())

    # valores únicos
    print("\n Servicios únicos:")
    print(df_limpio["nombre"].unique())