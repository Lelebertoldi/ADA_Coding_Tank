# 2) Faça um programa que peça um número e mostre se ele é positivo ou negativo. Alternativa: acrescentar nulo

numero = float(input("Digite um número: "))

if numero == 0:
    print("Nulo.")
    
elif numero > 0:
    print("Número positivo.")
    
else:
    print("Número negativo.")