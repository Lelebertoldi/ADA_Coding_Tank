'''5) Escreva um programa que peça a nota de 3 provas de um aluno e verifique
se ele passou ou não de ano.
Obs.: O aluno irá passar de ano se sua média for maior que 6.
'''

nota1 = float(input("Digite sua nota da primeira prova: "))
nota2 = float(input("Digite sua nota da segunda prova: "))
nota3 = float(input("Digite sua nota da terceira prova: "))

media = (nota1 + nota2 + nota3) / 3

if media > 6:
    print("Parabéns! Você passou de ano!")
    
else:
    print("Infelizmente você não passou de ano.")
