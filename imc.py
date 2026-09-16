"""
Proyecto-Python-IMC
Reto semanal 2 - Fundamentos de Python
Calcula el Índice de Masa Corporal (IMC) a partir de datos
ingresados dinámicamente por el usuario.
"""

# 1. Entrada dinámica de datos mediante input()
edad_input = input("Ingresa tu edad (años): ")
peso_input = input("Ingresa tu peso (kg): ")
estatura_input = input("Ingresa tu estatura (m): ")

# 2. Casting: edad a entero, peso y estatura a flotante
edad = int(edad_input)
peso = float(peso_input)
estatura = float(estatura_input)

# 3. Fórmula del IMC: IMC = peso / estatura^2
imc = peso / (estatura ** 2)

# Resultado
print(f"\n--- Resultado ---")
print(f"Edad: {edad} años")
print(f"Peso: {peso} kg")
print(f"Estatura: {estatura} m")
print(f"Tu IMC es: {imc:.2f}")

input()
#Solo es para que no cierre el programa de golpe
