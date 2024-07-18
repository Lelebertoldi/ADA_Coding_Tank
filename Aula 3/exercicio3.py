'''3) Faça um programa que imprima a tabuada do 9 na tela (entre 1 e 10).
Insira a conta, por exemplo, 9 * 1 = 9, sendo cada um dos valores em uma linha diferente.'''

contador = 1

while contador <= 10:
    multiplicacao = contador * 9
    print(f'9 * {contador} = {multiplicacao}')
    contador += 1