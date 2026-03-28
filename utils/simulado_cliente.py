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

        clientes.append(cliente)

    return clientes


# probar
print(generar_clientes(5))