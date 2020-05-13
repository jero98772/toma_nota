nombres = ["Jimmy", "Rosa", "Max", "Lina", "Juan", "Teresa"]

for nombre in nombres:
    if len(nombre) != 4:
        continue

    print(f"Hola, {nombre}")

    if nombre == "Lina":
        break
