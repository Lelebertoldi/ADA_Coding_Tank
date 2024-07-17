'''7) Vamos fazer um programa para verificar quem é o assassino de um crime. Para descobrir o 
assassino, a polícia faz um pequeno questionário com 5 perguntas 
onde a resposta só pode ser sim ou não:

a. Mora perto da vítima?

b. Já trabalhou com a vítima?

c. Telefonou para a vítima?

d. Esteve no local do crime?

e. Devia para a vítima?

Cada resposta sim dá um ponto para o suspeito. A polícia considera que os suspeitos com 5
pontos são os assassinos, com 4 a 3 pontos 
são cúmplices e 2 pontos são apenas suspeitos, necessitando outras investigações. Valores
iguais ou abaixo de 1 são liberados.'''

mora = input("Você mora perto da vítima? Responda com sim ou não:  ")
trabalhou = input("Já trabalhou com a vítima? Responda com sim ou não:  ")
telefonou = input("Telefonou para a vítima? Responda com sim ou não:  ")
local = input("Esteve no local do crime? Responda com sim ou não:  ")
devia = input("Devia para a vítima? Responda com sim ou não:  ")

if mora.upper() == 'SIM':
    suspeito1 = 1
    
else:
    suspeito1 = 0
    
if trabalhou.upper() == 'SIM':
    suspeito2 = 1
    
else:
    suspeito2 = 0
    
if telefonou.upper() == 'SIM':
    suspeito3 = 1

else:
    suspeito3 = 0
    
if local.upper() == 'SIM':
    suspeito4 = 1
    
else:
    suspeito4 = 0
    
if devia.upper() == 'SIM':
    suspeito5 = 1
    
else:
    suspeito5 = 0
    
julgamento = suspeito1 + suspeito2 + suspeito3 + suspeito4 + suspeito5

if julgamento == 5:
    print("Assassino.")
    
elif julgamento >= 3:
    print("Cúmplice.")
    
elif julgamento == 2:
    print("Suspeito, necessita outras investigações.")
    
else:
    print("Liberado.")
