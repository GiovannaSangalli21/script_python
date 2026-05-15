# Escreva um programa que peça um número de 1 a 10, e mostre a tabuada desse número.

num = int(input("Digite um número de a 10 para ver a tabuada: "))
if num < 1 or num > 10:
  print("Número errado! Digite apenas o número de 1 a 10")
else:
  print(f"Tabuada do {num}:")
  for i in range(1,11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")