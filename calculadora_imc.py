#datos de texto (string)
nombre = "eduardo"
apellido_paterno = "molina"
apellido_materno = "martinez"

# Revision de datos correctos (Edad)
while True:
    entrada_edad = input("¿Cuál es tu edad? ").strip()

    if not entrada_edad:
        print("Error: el campo de edad no puede estar vacío.")
        continue

    try:
        edad = int(entrada_edad)

        if edad <= 0:
            print("Error: la edad debe ser mayor que cero.")
            continue

        break

    except ValueError:
        print("Error: introduce una edad válida usando números enteros.")

# Validacion de datos correctos (Peso)
while True:
    entrada_peso = input("¿Cuánto pesas en kg? ").strip()

    if not entrada_peso:
        print("Error: el campo de peso no puede estar vacío.")
        continue

    try:
        peso = float(entrada_peso)

        if peso <= 0:
            print("Error: el peso debe ser mayor que cero.")
            continue

        break

    except ValueError:
        print("Error: introduce un peso válido usando números.")

# Validacion de datos correctos (Altura)
while True:
    entrada_estatura = input("¿Cuánto mides en metros? ").strip()

    if not entrada_estatura:
        print("Error: el campo de estatura no puede estar vacío.")
        continue

    try:
        estatura = float(entrada_estatura)

        if estatura <= 0:
            print("Error: la estatura debe ser mayor que cero.")
            continue

        break

    except ValueError:
        print("Error: introduce una estatura válida usando números.")

# Calculo de IMC
imc = peso / (estatura **2) 

# Formato de nombres y apellido
nombre = nombre.capitalize ()
apellido_paterno = apellido_paterno.capitalize()
apellido_materno = apellido_materno.capitalize()
# Muestra de resultados
print( "\n=== Resultados ===" )
print(f"\n¡Bienvenido, {nombre} {apellido_paterno} {apellido_materno}!")
print(f"Edad: {edad} años")
print(f"Peso: {peso} kg")
print(f"Estatura: {estatura} mts")
print(f"Tu IMC es de: {imc:.2f}")

