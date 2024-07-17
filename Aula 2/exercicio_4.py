"""
4) Faça um programa que leia a validade das informações:

a. Idade: entre 0 e 150;

b. Salário: maior que 0;

c. Sexo: M, F ou Outro;
O programa deve imprimir uma mensagem de erro para cada informação inválida.

    """
    
idade = int(input('Digite sua idade: '))
salario = float(input('Digite seu salário: '))
sexo = str(input('Digite seu sexo: '))

if idade > 0 and idade < 150:
    print('Válido')
    
else:
    print('Inválido')

if salario > 0:
    print('Válido')
    
else:
    print('Inválido')
    
if sexo == 'M' or 'F' or 'Outro':
    print('Válido')
    
else:
    print('Inválido')
