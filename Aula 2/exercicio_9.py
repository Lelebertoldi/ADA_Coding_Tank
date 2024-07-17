'''9) Desafio 1 - Faça um programa que leia 3 números e informe o maior deles.'''

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

maior = num1

if num2 > maior:
    maior = num2

if num3 > maior:
    maior = num3

print(f"O maior número é: {maior}")
