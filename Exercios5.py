# Faça um programa que leia e valide as seguintes informações:

nome = input("digite seu nome:")
while len(nome) <=3:
  nome=input("numeros de caracteres não suficiente, digite de novo:")

idade=int(input("digite sua idade:"))
while idade < 0 or idade > 150:
    idade =int(input("idade incorreta, tente novamente"))
salario = float(input("digite seu salario:"))
while salario <= 0:
      salario = float(input("salario incorreto, tente novamente:"))
sexo = input("digite seu sexo, 'f' ou 'm':")
while sexo != 'f' and sexo != 'm':
      sexo = input("sexo incorreto, tente novamente:")
estado_civil = input("digite seu estado civil, 's', 'c', 'v', 'd':")
while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
      estado_civil = input("estado civil incorreto, tente novamente:")
print("dados confimados, muito obrigada!")
