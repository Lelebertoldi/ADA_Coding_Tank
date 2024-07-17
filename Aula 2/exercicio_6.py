'''
6) Faça um programa que mostre uma questão de múltipla escolha com 5 opções 
(letras a, b, c, d, e). 
Sabendo a resposta certa, o programa deve receber a opção do usuário e informar a 
letra que o usuário marcou e se a resposta está certa ou errada.
'''

escolha = input("Escolha uma das opções: A, B, C, D ou E: ")

if escolha.upper() == "A":
    print(f"Você escolheu a opção {escolha}, sua resposta está correta!")
    
else:
    print(f"Você escolheu a opção {escolha}, sua resposta está errada!")
