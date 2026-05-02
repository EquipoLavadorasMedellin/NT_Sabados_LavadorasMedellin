import pandas as pd

def describir_clientes(df_limpio):
    print("/Descripción del DataFrame de Clientes/")

    print(f"numero de filas: {df_limpio.shape[0]}")
    print(f"numero de columnas: {df_limpio.shape[1]}")
    print(f"columnas disponibles: {list(df_limpio.columns)}")
    print(f"tipos de datos de cada atributo: {df_limpio.dtypes}")

    #conteos importantes
    print("/conteos/")

    # valores categóricos
    print("\n Frecuencia de clientes:")
    print(df_limpio["nombre"].value_counts())
    
