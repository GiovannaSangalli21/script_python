# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1. Dica: Utilize o operador aritmético %, que retorna o resto da divisão de dois números.


# 6
numero = int(input("digite um numero inteiro: "))
primo = True 
if numero <= 1:
 primo = False 
else: 
   for i in range (2, numero): 
      if numero % i == 0:
       primo = False 
if primo :
  print(f"O numero {numero} é primo.")
else:
  print(f"o numero {numero} não é primo.")
