#datos de texto (string)
nombre = "Eduardo"
apellido_paterno = "molina"
apellido_materno = "martinez"
#datos en numero entero (int)
edad = int(input("cual es tu edad? "))
#datos en numero decimal (float)
peso = float(input("cuanto pesas? "))
estatura = float(input("Cuanto mides? "))
imc = peso / (estatura **2) 
#prueba para muestra de datos
print( "=== Resultados ===" )
print("\n!Bienvenido",)
print(nombre, apellido_paterno, apellido_materno)
print("Edad", edad, "años")
print("Peso", peso, "kg")
print("Altura", estatura, "mts")
print("Tu imc es de", round(imc,(2)))
