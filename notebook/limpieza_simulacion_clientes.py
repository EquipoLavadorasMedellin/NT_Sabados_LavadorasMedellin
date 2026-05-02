import pandas as pd
#id_cliente num
#nombre string
#tel string
#direccion string
#email string


def limpiar_datos_clientes(df_sucio):
    df_limpio = df_sucio.copy()
    
    #0 renombrar columnas
    df_limpio = df_limpio.rename(columns={"id_cliente": "id", "telefono": "tel"})
    
    #1 limpiar las col de string
    col_text=["nombre", "tel", "direccion", "email"]
    for col in col_text:
        df_limpio[col] = df_limpio[col].astype("string").str.strip().str.lower()
    
    #1.1 limpiar ide_cliente para que sea numérico
    df_limpio["id"] = pd.to_numeric(df_limpio["id"])

    #1.2 definir valores validos para cada col
    valores_validos_tel = (df_limpio["tel"].str.match(r"^\d{10}$"))
    valores_validos_email = (df_limpio["email"].str.match(r"^[\w\.-]+@[\w\.-]+\.\w+$"))

    #1.3 aplicar filtros
    df_limpio["tel"] = df_limpio["tel"].where(valores_validos_tel, pd.NA)
    df_limpio["email"] = df_limpio["email"].where(valores_validos_email,pd.NA)

    #2 definir numeros esperados
    df_limpio=df_limpio[df_limpio["id"]>0]

    #3 eliminar registros obligatorios vacios
    df_limpio = df_limpio.dropna(subset=["nombre", "tel", "direccion", "email"])

    #4 eliminar registros duplicados
    df_limpio = df_limpio.drop_duplicates()
    
    return df_limpio
