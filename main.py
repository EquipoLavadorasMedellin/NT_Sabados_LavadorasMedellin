import pandas as pd

#Clientes
from utils.simulado_cliente import generar_clientes
from notebook.limpieza_simulacion_clientes import limpiar_datos_clientes

#Servicios
from utils.simulacion_servicio import generar_servicios
from notebook.limpieza_servicio import limpiar_servicios 

#Descripciones 
from notebook.descripcion_servicio import describir_servicios
from notebook.descripcion_simulacion_cliente import describir_clientes
#mostrar clientes
print("=" * 60)
print("GENERANDO CLIENTES")
print("=" * 60)
data = generar_clientes(5)

df = pd.DataFrame(data)
print(f" Clientes generados: {len(df)}")
print(f"Columnas: {list(df.columns)}")
print(f"\n{df}\n")

print("Guardando clientes sucios...")
df.to_csv("data/clientes_sucios.csv", index=False, encoding="utf-8")
df.to_json(
    "data/clientes_sucios.json", 
    orient="records", 
    force_ascii=False,
    indent=4
    )
print(" Clientes sucios guardados en CSV y JSON\n")

#limpiar clientes
print("=" * 60)
print("LIMPIANDO CLIENTES")
print("=" * 60)
df_limpio = limpiar_datos_clientes(df)
print(f" Clientes limpios: {len(df_limpio)}")
print(f"Columnas: {list(df_limpio.columns)}")
print(f"\n{df_limpio}\n")

print("Guardando clientes limpios...")
df_limpio.to_csv("data/clientes_limpios.csv", index=False, encoding="utf-8")

df_limpio.to_json(
    "data/clientes_limpios.json", 
    orient="records", 
    force_ascii=False,
    indent=4
)
print(" Clientes limpios guardados en CSV y JSON\n")

#mostrar servicios
print("=" * 60)
print("GENERANDO SERVICIOS")
print("=" * 60)
data_servicios = generar_servicios(5)

df_servicios= pd.DataFrame(data_servicios)
print(f" Servicios generados: {len(df_servicios)}")
print(f"Columnas: {list(df_servicios.columns)}")
print(f"\n{df_servicios}\n")

#guardar sucio
print("Guardando servicios sucios...")
df_servicios.to_csv("data/servicios_sucios.csv", index=False , encoding="utf-8")

df_servicios.to_json(
    "data/servicios_sucios.json", 
    orient="records", 
    force_ascii=False,
    indent=4
    )
print(" Servicios sucios guardados en CSV y JSON\n")

#limpiar servicios
print("=" * 60)
print("LIMPIANDO SERVICIOS")
print("=" * 60)
df_servicios_limpio = limpiar_servicios(df_servicios)
print(f" Servicios limpios: {len(df_servicios_limpio)}")
print(f"Columnas: {list(df_servicios_limpio.columns)}")
print(f"\n{df_servicios_limpio}\n")

print("Guardando servicios limpios...")
df_servicios_limpio.to_csv("data/servicios_limpios.csv", index=False, encoding="utf-8")

df_servicios_limpio.to_json(
    "data/servicios_limpios.json", 
    orient="records", 
    force_ascii=False,
    indent=4
)
print(" Servicios limpios guardados en CSV y JSON\n")

#describir servicios
print("=" * 60)
print("DESCRIPCIÓN SERVICIOS LIMPIOS")
print("=" * 60)
describir_servicios(df_servicios_limpio)

print("\n" + "=" * 60)
print("DESCRIPCIÓN CLIENTES")
print("=" * 60)
describir_clientes(df_limpio)