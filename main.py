import pandas as pd

# ============================================================
# SECCIÓN 1: SIMULACIÓN Y LIMPIEZA LOCAL (código existente)
# ============================================================

# --- Clientes ---
from utils.simulado_cliente import generar_clientes
from notebook.limpieza_simulacion_clientes import limpiar_datos_clientes

# --- Servicios ---
from utils.simulacion_servicio import generar_servicios
from notebook.limpieza_servicio import limpiar_servicios 

# --- Descripciones ---
from notebook.descripcion_servicio import describir_servicios
from notebook.descripcion_simulacion_cliente import describir_clientes

# mostrar clientes
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

# limpiar clientes
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

# mostrar servicios
print("=" * 60)
print("GENERANDO SERVICIOS")
print("=" * 60)
data_servicios = generar_servicios(5)

df_servicios= pd.DataFrame(data_servicios)
print(f" Servicios generados: {len(df_servicios)}")
print(f"Columnas: {list(df_servicios.columns)}")
print(f"\n{df_servicios}\n")

# guardar sucio
print("Guardando servicios sucios...")
df_servicios.to_csv("data/servicios_sucios.csv", index=False , encoding="utf-8")

df_servicios.to_json(
    "data/servicios_sucios.json", 
    orient="records", 
    force_ascii=False,
    indent=4
    )
print(" Servicios sucios guardados en CSV y JSON\n")

# limpiar servicios
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

# describir servicios
print("=" * 60)
print("DESCRIPCIÓN SERVICIOS LIMPIOS")
print("=" * 60)
describir_servicios(df_servicios_limpio)

print("\n" + "=" * 60)
print("DESCRIPCIÓN CLIENTES")
print("=" * 60)
describir_clientes(df_limpio)


# ============================================================
# SECCIÓN 2: CONSUMO DE API + TRANSFORMACIÓN + GRAFICACIÓN
# ============================================================
# Esta sección se conecta al backend Spring Boot (localhost:8080),
# trae los datos de cada tabla, aplica transformaciones con pandas,
# y genera gráficas con matplotlib.
#
# IMPORTANTE: Para que esta sección funcione, el backend debe
# estar corriendo en http://localhost:8080
# ============================================================

# --- Importar consumidores de API ---
from utils.consumir_api_servicio import consumir_servicios
from utils.consumir_api_cliente import consumir_clientes
from utils.consumir_api_reserva import consumir_reservas
from utils.consumir_api_tecnico import consumir_tecnicos

# --- Importar transformaciones ---
from notebook.transformacion_servicio import transformar_datos_servicios
from notebook.transformacion_cliente import transformar_datos_clientes
from notebook.transformacion_reserva import transformar_datos_reservas
from notebook.transformacion_tecnico import transformar_datos_tecnicos

# --- Importar módulo de graficación ---
from notebook.graficacion import (
    graficar_barras,
    graficar_lineas,
    graficar_torta,
    graficar_dispersion
)

print("\n" + "=" * 60)
print("CONSUMO DE API Y ANALÍTICA DE DATOS")
print("=" * 60)

try:
    # ──────────────────────────────────────────────────────────
    # TABLA SERVICIO
    # ──────────────────────────────────────────────────────────
    print("\n--- SERVICIOS (desde API) ---")
    datos_servicios_api = consumir_servicios()
    print(f"Servicios obtenidos de la API: {len(datos_servicios_api)}")

    if len(datos_servicios_api) > 0:
        resultado_servicios = transformar_datos_servicios(datos_servicios_api)

        # 1. Conteo Mantenimiento (Barras)
        if len(resultado_servicios["conteoMantenimiento"]) > 0:
            graficar_barras(resultado_servicios["conteoMantenimiento"], "nombre", "conteo", "Servicios de Mantenimiento", "servicio_mantenimiento")

        # 2. Sumatoria Servicios Caros (Torta)
        if len(resultado_servicios["sumatoriaServiciosCaros"]) > 0:
            graficar_torta(resultado_servicios["sumatoriaServiciosCaros"], "nombre", "sumatoria", "Costo Servicios Caros (>= 100k)", "servicio_caros")

        # 3. Promedio de precios (Barras Horizontales)
        if len(resultado_servicios["promedioPreciosPorServicio"]) > 0:
            graficar_barras(resultado_servicios["promedioPreciosPorServicio"], "nombre", "promedio", "Promedio de Precios", "servicio_promedio", horizontal=True)

        # 4. Conteo Reparaciones por descripción (Líneas)
        if len(resultado_servicios["conteoReparaciones"]) > 0:
            graficar_lineas(resultado_servicios["conteoReparaciones"], "descripcion", "conteo", "Tipos de Reparación", "servicio_reparaciones")

        # 5. Conteo General de Servicios (Dispersión)
        if len(resultado_servicios["conteoGeneralServicios"]) > 0:
            graficar_dispersion(resultado_servicios["conteoGeneralServicios"], "nombre", "conteo", "Conteo General de Servicios", "servicio_general")

    # ──────────────────────────────────────────────────────────
    # TABLA CLIENTE
    # ──────────────────────────────────────────────────────────
    print("\n--- CLIENTES (desde API) ---")
    datos_clientes_api = consumir_clientes()
    print(f"Clientes obtenidos de la API: {len(datos_clientes_api)}")

    if len(datos_clientes_api) > 0:
        resultado_clientes = transformar_datos_clientes(datos_clientes_api)

        if len(resultado_clientes["clientesMayoresA5PorDireccion"]) > 0:
            graficar_barras(resultado_clientes["clientesMayoresA5PorDireccion"], "direccion", "conteo", "Clientes > 5 por Dirección", "cliente_mayores5")

        if len(resultado_clientes["clientesMenoresA5PorNombre"]) > 0:
            graficar_torta(resultado_clientes["clientesMenoresA5PorNombre"], "nombre", "conteo", "Clientes <= 5 por Nombre", "cliente_menores5")

        if len(resultado_clientes["conteoGeneralPorDireccion"]) > 0:
            graficar_barras(resultado_clientes["conteoGeneralPorDireccion"], "direccion", "conteo", "General por Dirección", "cliente_direccion", horizontal=True)

        if len(resultado_clientes["conteoGeneralPorNombre"]) > 0:
            graficar_lineas(resultado_clientes["conteoGeneralPorNombre"], "nombre", "conteo", "Conteo General por Nombre", "cliente_nombre")

        if len(resultado_clientes["conteoGeneralPorTelefono"]) > 0:
            graficar_dispersion(resultado_clientes["conteoGeneralPorTelefono"], "telefono", "conteo", "Conteo General por Teléfono", "cliente_telefono")

    # ──────────────────────────────────────────────────────────
    # TABLA RESERVA
    # ──────────────────────────────────────────────────────────
    print("\n--- RESERVAS (desde API) ---")
    datos_reservas_api = consumir_reservas()
    print(f"Reservas obtenidas de la API: {len(datos_reservas_api)}")

    if len(datos_reservas_api) > 0:
        resultado_reservas = transformar_datos_reservas(datos_reservas_api)

        if len(resultado_reservas["reservasMananaPorEstado"]) > 0:
            graficar_barras(resultado_reservas["reservasMananaPorEstado"], "estado", "conteo", "Reservas Mañana por Estado", "reserva_manana")

        if len(resultado_reservas["reservasPendientesPorJornada"]) > 0:
            graficar_lineas(resultado_reservas["reservasPendientesPorJornada"], "jornada", "conteo", "Reservas Pendientes", "reserva_pendientes")

        if len(resultado_reservas["reservasTardePorEstado"]) > 0:
            graficar_torta(resultado_reservas["reservasTardePorEstado"], "estado", "conteo", "Reservas Tarde", "reserva_tarde")

        if len(resultado_reservas["conteoGeneralPorFecha"]) > 0:
            graficar_barras(resultado_reservas["conteoGeneralPorFecha"], "fechaReserva", "conteo", "General por Fecha", "reserva_fecha", horizontal=True)

        if len(resultado_reservas["conteoGeneralPorEstado"]) > 0:
            graficar_dispersion(resultado_reservas["conteoGeneralPorEstado"], "estado", "conteo", "General por Estado", "reserva_estado")

    # ──────────────────────────────────────────────────────────
    # TABLA TECNICO
    # ──────────────────────────────────────────────────────────
    print("\n--- TÉCNICOS (desde API) ---")
    datos_tecnicos_api = consumir_tecnicos()
    print(f"Técnicos obtenidos de la API: {len(datos_tecnicos_api)}")

    if len(datos_tecnicos_api) > 0:
        resultado_tecnicos = transformar_datos_tecnicos(datos_tecnicos_api)

        if len(resultado_tecnicos["tecnicosActivosPorDescripcion"]) > 0:
            graficar_barras(resultado_tecnicos["tecnicosActivosPorDescripcion"], "descripcion", "conteo", "Técnicos Activos por Especialidad", "tecnico_activos")

        if len(resultado_tecnicos["tecnicosNuevosPorNombre"]) > 0:
            graficar_torta(resultado_tecnicos["tecnicosNuevosPorNombre"], "nombre", "conteo", "Técnicos < 5 por Nombre", "tecnico_nuevos")

        if len(resultado_tecnicos["conteoGeneralPorEmail"]) > 0:
            graficar_barras(resultado_tecnicos["conteoGeneralPorEmail"], "email", "conteo", "Técnicos por Email", "tecnico_email", horizontal=True)

        if len(resultado_tecnicos["conteoGeneralPorNombre"]) > 0:
            graficar_lineas(resultado_tecnicos["conteoGeneralPorNombre"], "nombre", "conteo", "Conteo por Nombre", "tecnico_nombre")

        if len(resultado_tecnicos["tecnicosAntiguosPorDescripcion"]) > 0:
            graficar_dispersion(resultado_tecnicos["tecnicosAntiguosPorDescripcion"], "descripcion", "conteo", "Técnicos Antiguos por Especialidad", "tecnico_antiguos")

    print("\n" + "=" * 60)
    print("ANÁLISIS COMPLETO")
    print("=" * 60)

except Exception as e:
    print(f"\n⚠️  Error al conectar con la API o al graficar: {e}")
    print("Asegúrate de que el backend esté corriendo en http://localhost:8080")