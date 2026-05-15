# Utilizando o laço While faça um programa que peça uma senha ao usuário, e que imprima "Acesso liberado" apenas se o usuário digitar a senha corretamente. A senha devera ser a seguinte senha númerica : "676767".

senha_correta = "676767"

senha_digitada = ""

while senha_digitada != senha_correta:
  senha_digitada = input("Digite a senha: ")
  if senha_digitada != senha_correta:
   print("Senha incorreta! Tente novamente")
print("Acesso liberado")

