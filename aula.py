numero1 = int(input("Digita um numero ai: "))
numero2 = int(input("Outro numero porfavor: "))
numero3 = int(input("Mais um numero: "))

#Assumimos temporariamente que o primeiro numero é o maior deles 
# jaja a gente verifica isso

maior_numero = numero1

#agora verificaremos se o segundo numero é maior do que o maior numero atual
#caso for atualizaremos o maior numero

if numero2 > maior_numero:
    maior_numero = numero2

#fazemos o mesmo processo com o numero 3 

if numero3 > maior_numero:
    maior_numero = numero3


print("O maior numero é : ", maior_numero)








