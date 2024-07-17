'''8) Um produto vai sofrer aumento de acordo com a Tabela 1 abaixo. Faça um programa que peça 
para o usuário digitar o valor do produto de acordo 
com o preço antigo e escreva uma das mensagens da Tabela 2, de acordo com o preço reajustado:

Tabela 1

| Preço Antigo         | % de aumento |
|----------------------|--------------|
| Até 50 reais         | 5%           |
| Entre 50 e 100 reais | 10%          |
| De 100 a 150 reais   | 13%          |
| Acima de 150 reais   | 15%          |
Tabela 2

| Preço Novo            | Mensagem   |
|-----------------------|------------|
| Até 80 reais          | Barato     |
| Entre 80 e 115 reais  | Razoável   |
| Entre 115 e 150 reais | Normal     |
| Entre 150 e 170 reais | Caro       |
| Acima de 170 reais    | Muito Caro |'''

preco_antigo = float(input("Digite o valor do produto: "))

if preco_antigo <= 50:
    aumento = 0.05  # 5%
elif preco_antigo <= 100:
    aumento = 0.10  # 10%
elif preco_antigo <= 150:
    aumento = 0.13  # 13%
else:
    aumento = 0.15  # 15%

valor_aumentado = preco_antigo * (1 + aumento)

if valor_aumentado <= 80:
    print("Barato")
elif valor_aumentado <= 115:
    print("Razoável")
elif valor_aumentado <= 150:
    print("Normal")
elif valor_aumentado <= 170:
    print("Caro")
else:
    print("Muito Caro")
