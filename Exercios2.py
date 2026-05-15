# Escreva um script que leia três números e mostre o maior e o menor deles.

# Exercio 2
x1 = int(input("Digite o primeiro número:"))
x2 = int(input("Digite o segundo número:"))
x3 = int(input("Digite o terceiro número:"))

if x1 >= x2 and x1 >= x3:
  maior = x1
  if x2 >= x3:
    meio = x2
    menor = x3
  else:
    meio = x3
    menor = x2
elif x2 >= x1 and x2 >= x3:
  maior = x2
  if n1 >= x3:
   meio = x1
   menor = x3
  else:
   meio = x3
   menor = x1
else:
  maior = x3
  if n2 > x1:
    meio = x2
    menor = x1
  else:
    meio = x2
    menor = x1
print(f"O menor número é: {menor}")
print(f"O maior número é: {maior}")

