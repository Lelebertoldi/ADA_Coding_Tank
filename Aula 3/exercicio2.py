'''2) Faça um programa que mostre o fatorial de um número digitado.  
_Exemplo_  
número digitado: 5  
resultado esperado: 120'''



numero = int(input("Digite um número: "))

contador = 1
resposta = 1

while contador <= numero:
    resposta *= contador
    contador += 1
    
print(resposta)