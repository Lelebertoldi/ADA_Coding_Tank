'''6) Faça uma calculadora. O usuário deve inserir qual a operação matemática ele deseja
realizar e logo em seguida os dois números. O programa deve finalizar apenas quando o
usuário digitar a opção "sair" no momento de escolha da operação matemática.'''

while True:
    operacao = input("Digite a operação desejada (+, -, *, /) ou 'sair' para encerrar: ").lower()

    if operacao == 'sair':
        print("Programa encerrado.")
        break

    if operacao == '+' or operacao == '-' or operacao == '*' or operacao == '/':
        
        while True:
            num1_str = input("Digite o primeiro número: ")
            if num1_str.isdigit(): # se numero digitado for numero
                num1 = float(num1_str) # transforma a string para numero flutuante
                break
            else:
                print("Entrada inválida. Por favor, insira um número válido.")

        while True:
            num2_str = input("Digite o segundo número: ")
            if num2_str.isdigit(): # se numero digitado for numero
                num2 = float(num2_str) # transforma a string para numero flutuante
                break
            else:
                print("Entrada inválida. Por favor, insira um número válido.")

        if operacao == '+':
            resultado = num1 + num2
            print(f"{num1} + {num2} : {resultado}")
        elif operacao == '-':
            resultado = num1 - num2
            print(f"{num1} - {num2} : {resultado}")
        elif operacao == '*':
            resultado = num1 * num2
            print(f"{num1} * {num2} : {resultado}")
        elif operacao == '/':
            if num2 == 0:
                print("Erro: Divisão por zero não é permitida.")
            else:
                resultado = num1 / num2
                print(f"{num1} / {num2} : {resultado}")

    else:
        print("Operação inválida. Por favor, escolha uma das operações válidas: +, -, *, /")
