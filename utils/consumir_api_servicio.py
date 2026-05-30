# ============================================================
# CONSUMO DE API — TABLA SERVICIO
# ============================================================
# Este archivo se conecta al backend Spring Boot y trae
# todos los registros de la tabla "servicio".
# Pasos:
#   1. Almacenar la URL del endpoint en una variable
#   2. Activar el requests (hacer la petición GET)
#   3. Esperar el status code (raise_for_status)
#   4. Verificar el formato de respuesta (.json())
#   5. Retornar la respuesta
# ============================================================

import requests

def consumir_servicios():
    # 1. Almacenar la URL + endpoint en una variable
    url = "http://localhost:8080/servicios"

    # 2. Activar el requests (petición GET)
    respuesta = requests.get(url)

    # 3. Esperar el status code
    respuesta.raise_for_status()  # Lanza error si no es 200

    # 4. Verificar el formato de respuesta
    datos = respuesta.json()

    # 5. Retornar la respuesta
    return datos


# Prueba rápida (solo se ejecuta si corres este archivo directamente)
if __name__ == "__main__":
    print(consumir_servicios())
