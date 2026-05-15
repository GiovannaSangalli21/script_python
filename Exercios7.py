# Faça um algoritmo utilizando o laço FOR que descreva o Fatorial de um número digitado pelo usuário.

# 7
num = int(input("Digite um numero fatorial: "))
fatorial = 1 
if num < 0:
  print("Esse número não é fatorial")
elif num == 0:
  print("o fatorial de 0 e 1")
else :
  for i in range (1,num +1):
      fatorial = fatorial * i
  print(f"o fatorial de {num} é {fatorial} ")

