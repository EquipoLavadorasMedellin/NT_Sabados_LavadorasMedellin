import pandas as pd
from utils.simulado_cliente import generar_clientes

data = generar_clientes(5)

df = pd.DataFrame(data)
df.to_csv("data/clientes_sucios.csv", index=False, encoding="utf-8")

df.to_json(
    "data/clientes_sucios.json", 
    orient="records", 
    force_ascii=False,
    indent=4
    )