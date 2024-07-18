'''4) Faça um programa em que o usuário digite números quaisquer e encerrará 
no momento em que o valor 0 seja digitado. Ao final diga qual foi o maior número digitado.'''


numero = int(input('Digite um número: '))

maior = numero

while numero != 0:
    numero = int(input('Digite um novo número ou digite 0 para sair: '))
    if numero > maior:
        maior = numero
        
print(f"O maior número digitado é: {maior} ")
