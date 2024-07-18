'''5) Faça um script que peça para o usuário digitar a idade, o salário e o sexo de uma pessoa 
até que as entradas digitadas sejam válidas.

a. Idade: entre 0 e 150
b. Salário: maior que 0
c. Gênero: M, F ou Outro'''

while True:
    idade = input("Digite uma idade (entre 0 e 150): ")
    if idade.isdigit(): # se a idade for numero
        idade = int(idade) # converte a str para int
        if 0 <= idade <= 150:
            break
        else:
            print("Idade inválida. A idade deve estar entre 0 e 150.")
    else:
        print("Entrada inválida. Por favor, digite um número inteiro.")

while True:
    salario = input("Digite o salário (inteiro e maior que 0): ")
    if salario.isdigit(): # se o salario for numero
        salario = int(salario) # converte a str para int
        if salario > 0:
            break
        else:
            print("Salário inválido. O salário deve ser maior que 0.")
    else:
        print("Entrada inválida. Por favor, digite um número válido.")

while True:
    genero = input("Digite o gênero (M, F ou Outro): ").upper() 
    if genero == 'M' or genero == 'F' or genero == 'OUTRO':
        break
    else:
        print("Gênero inválido. Digite 'M' para Masculino, 'F' para Feminino ou 'Outro': ")
