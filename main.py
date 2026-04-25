import pandas as pd

#Clientes
from utils.simulado_cliente import generar_clientes

#Servicios
from utils.simulacion_servicio import generar_servicios
from notebook.limpieza_servicio import limpiar_servicios 

#Descripciones 
from notebook.descripcion_servicio import describir_servicios

#mostrar clientes
data = generar_clientes(5)

df = pd.DataFrame(data)
df.to_csv("data/clientes_sucios.csv", index=False, encoding="utf-8")

df.to_json(
    "data/clientes_sucios.json", 
    orient="records", 
    force_ascii=False,
    indent=4
    )

#mostrar servicios
data_servicios = generar_servicios(5)

df_servicios= pd.DataFrame(data_servicios)

#guardar sucio
df_servicios.to_csv("data/servicios_sucios.csv", index=False , encoding="utf-8")

df_servicios.to_json(
    "data/servicios_sucios.json", 
    orient="records", 
    force_ascii=False,
    indent=4
    )

#limpiar servicios
df_servicios_limpio = limpiar_servicios(df_servicios)

df_servicios_limpio.to_csv("data/servicios_limpios.csv", index=False, encoding="utf-8")

df_servicios_limpio.to_json(
    "data/servicios_limpios.json", 
    orient="records", 
    force_ascii=False,
    indent=4
)

#describir servicios

print("\nDESCRIPCIÓN SERVICIOS LIMPIOS")
describir_servicios(df_servicios_limpio)