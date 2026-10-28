#datos de texto (string)
nombre = "eduardo"
apellido_paterno = "molina"
apellido_materno = "martinez"
#datos en numero entero (int)
edad = int(input("cual es tu edad? "))
#datos en numero decimal (float)
peso = float(input("cuanto pesas? "))
estatura = float(input("Cuanto mides? "))
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

