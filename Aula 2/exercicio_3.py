# 3) Faça um programa que peça dois números e mostre o maior deles.

numero1 = float(input("Digite um numero: "))
numero2 = float(input("Digite outro numero: "))

if numero1 > numero2:
    print(f"O maior número é: {numero1}")
  
elif numero2 > numero1:
    print(f'O maior número é: {numero2}')
    
else:
    print("Os numeros são iguais.")