import random

from faker import Faker

fake = Faker('es_CO')  

def generar_clientes(num_clientes):
    clientes = []

    for _ in range(num_clientes):
        cliente = {
            "id_cliente": fake.unique.random_int(min=1, max=1000),
            "nombre": fake.name(),
            "email": fake.email(),
            "telefono": fake.phone_number(),
            "direccion": fake.address(),
        }

        def ensuciar_dato(cliente):
    # Probabilidad de ensuciar cada campo
            if random.random() < 0.2:
                cliente["email"] = "correo_invalido.com"

            elif random.random() < 0.2:
                cliente["nombre"] = cliente["nombre"].lower()

            elif random.random() < 0.2:
                cliente["telefono"] = "123"

            elif random.random() < 0.1:
                cliente["direccion"] = None

            return cliente


        cliente = ensuciar_dato(cliente)
        clientes.append(cliente)

    return clientes

