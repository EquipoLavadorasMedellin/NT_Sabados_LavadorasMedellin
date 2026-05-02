# rutina simulacion simula cada dato de mi tabla, pone "semilla", dentro de un ciclo un diccionario para cada elemento que toco y se devuelve
import random

def generar_servicios(num_servicios):
    servicios = []

    nombres = [
        "Mantenimiento",
        "Diagnostico",
        "Reparacion"
    ]

    descripciones = [
        "Servicio de mantenimiento preventivo",
        "Diagnóstico completo de la lavadora",
        "Reparación y reemplazo de componentes"
    ]

    precios = [130, 40, None]

    for _ in range(num_servicios):
        servicio = {
            "id_servicio": random.randint(1, 1000),
            "nombre": random.choice(nombres),
            "descripcion": random.choice(descripciones),
            "precio_base": random.choice(precios)
        }

        # Inyección de errores 
        prob = random.random()

        if prob < 0.2:
            servicio["id_servicio"] = None

        elif prob < 0.4:
            servicio["nombre"] = random.choice(["servicio X", "otro servicio raro"])

        elif prob < 0.6:
            servicio["precio_base"] = random.choice([0, -50000, None])

        elif prob < 0.8:
            servicio["nombre"] = " " + servicio["nombre"].upper()

        elif prob < 0.9:
            servicio["descripcion"] = None

        servicios.append(servicio)

    return servicios