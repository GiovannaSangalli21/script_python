# Guia de Exercícios Resolvidos e Comentados em Python

- Este documento reúne a explicação lógica e o código fonte comentado de 10 exercícios práticos em Python. Os códigos foram revisados e corrigidos para garantir o funcionamento ideal.
  
### Exercício 1: Par ou Ímpar (0 a 100)
- **Funcionamento:** O programa gera uma sequência numérica de 0 a 100 e utiliza o operador de resto da divisão (`%`) para classificar cada número. Se o resto da divisão por 2 for zero, o número é par; caso contrário, é ímpar.

```python
# Laço de repetição que vai de 0 até 100 (o número 101 indica o limite superior exclusivo)
for i in range(101): 
    # Verifica se o resto da divisão do número atual (i) por 2 é igual a 0
    if i % 2 == 0:
        # Se for 0, o número é divisível por 2, logo é par
        print(f"{i} é par")
    else:
        # Caso contrário, o número não é divisível por 2, logo é ímpar
        print(f"{i} é ímpar")
```

### Exercício 2: Maior e Menor de Três Números
- **Funcionamento:** Compara três números informados pelo usuário. Ele valida sistematicamente as condições para ordenar e isolar qual variável guarda o maior, o menor e o valor do meio.

```python
# Solicita os três números ao usuário e os converte de texto (string) para inteiros (int)
x1 = int(input("Digite o primeiro número: "))
x2 = int(input("Digite o segundo número: "))
x3 = int(input("Digite o terceiro número: "))

# Estrutura condicional para testar se x1 é o maior de todos
if x1 >= x2 and x1 >= x3:
    maior = x1
    # Se x1 é o maior, resta descobrir a ordem entre x2 e x3
    if x2 >= x3:
        meio = x2
        menor = x3
    else:
        meio = x3
        menor = x2

# Se x1 não for o maior, testa se x2 é o maior de todos (Correção: n1 alterado para x1)
elif x2 >= x1 and x2 >= x3:
    maior = x2
    # Se x2 é o maior, resta descobrir a ordem entre x1 e x3
    if x1 >= x3:
        meio = x1
        menor = x3
    else:
        meio = x3
        menor = x1

# Se nem x1 nem x2 forem os maiores, obrigatoriamente x3 é o maior (Correção: lógica ajustada)
else:
    maior = x3
    # Se x3 é o maior, resta descobrir a ordem entre x1 e x2
    if x1 >= x2:
        meio = x1
        menor = x2
    else:
        meio = x2
        menor = x1

# Exibe os resultados finais encontrados na tela
print(f"O menor número é: {menor}")
print(f"O maior número é: {maior}")
```
### Exercício 3: Nome em Escada
- **Funcionamento:** Exibe o nome do usuário de forma progressiva linha por linha. O algoritmo utiliza fatiamento de strings (slicing) para aumentar o número de caracteres impressos a cada rodada do laço.

```python
# Recebe a string contendo o nome digitado pelo usuário
nome = input("Digite seu nome: ")

# O laço percorre de 1 até o tamanho total do nome + 1 (garantindo que a última letra apareça)
for i in range(1, len(nome) + 1):
    # Imprime um pedaço (fatia) da string, indo do início (índice 0) até a posição 'i'
    print(nome[:i])
```
### Exercício 4: Sequência de Fibonacci
- **Funcionamento:** Gera os primeiros $n$ termos da sequência matemática onde cada número subsequente é a soma dos dois anteriores. Ele armazena os valores em uma lista dinâmica ([]).

```python
# Pergunta ao usuário quantos números da sequência ele deseja gerar
n = int(input("Até qual termo você quer gerar? "))

# Define os dois valores iniciais da sequência matemática de Fibonacci
a, b = 0, 1  
# Cria uma lista vazia para armazenar os números conforme forem gerados
sequencia = []

# Laço que executa exatamente 'n' vezes (o caractere '_' indica que a variável do loop não será usada)
for _ in range(n):
    # Adiciona o valor atual de 'a' no final da nossa lista
    sequencia.append(a)
    # Atualização simultânea: 'a' recebe o valor de 'b', e 'b' recebe a soma de 'a + b' anteriores
    a, b = b, a + b  

# Imprime na tela a lista completa preenchida com a sequência gerada
print(f"Série de Fibonacci: {sequencia}")
```

### Exercício 5: Validação de Dados
- **Funcionamento:** Cria barreiras de segurança usando laços while. O programa recusa dados inválidos e repete a pergunta até que o usuário insira uma informação coerente com as regras definidas.

```python
# Solicita o nome e valida se tem mais de 3 caracteres
nome = input("Digite seu nome: ")
while len(nome) <= 3:
    nome = input("Número de caracteres não suficiente, digite de novo: ")

# Solicita a idade e valida se ela está no intervalo realista entre 0 e 150 anos
idade = int(input("Digite sua idade: "))
while idade < 0 or idade > 150:
    idade = int(input("Idade incorreta, tente novamente: "))

# Solicita o salário e valida se ele é um valor positivo (maior que zero)
salario = float(input("Digite seu salário: "))
while salario <= 0:
    salario = float(input("Salário incorreto, tente novamente: "))

# Solicita o sexo e aceita estritamente apenas os caracteres literais 'f' ou 'm'
sexo = input("Digite seu sexo, 'f' ou 'm': ")
while sexo != 'f' and sexo != 'm':
    sexo = input("Sexo incorreto, tente novamente: ")

# Solicita o estado civil e valida se corresponde a uma das iniciais permitidas
estado_civil = input("Digite seu estado civil, 's', 'c', 'v', 'd': ")
while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
    estado_civil = input("Estado civil incorreto, tente novamente: ")

# Mensagem disparada somente após todas as validações dos 'while' passarem com sucesso
print("Dados confirmados, muito obrigada!")
```

### Exercício 6: Verificador de Números Primos
- **Funcionamento:** Um número primo é divisível apenas por 1 e por si mesmo. O algoritmo assume que o número é primo (True) e tenta derrubar essa hipótese testando divisões por todos os números intermediários.

```python
# Solicita um número inteiro ao usuário
numero = int(input("Digite um número inteiro: "))
# Cria uma variável booleana de controle (flag), assumindo inicialmente que o número é primo
primo = True 

# Números menores ou iguais a 1 não são primos por definição
if numero <= 1:
    primo = False 
else: 
    # Testa os divisores possíveis partindo de 2 até o número anterior a ele (numero - 1)
    for i in range(2, numero): 
        # Se encontrar qualquer número onde o resto da divisão seja 0, significa que não é primo
        if numero % i == 0:
            primo = False 
            break # Interrompe o laço imediatamente, poupando processamento

# Estrutura condicional para exibir o resultado baseado na nossa variável de controle
if primo:
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo.")
```

### Exercício 7: Cálculo de Fatorial
- **Funcionamento:** Multiplica um número inteiro positivo por todos os seus antecessores até o número 1 utilizando um acumulador multiplicativo em um laço for.

```python
# Solicita o número inteiro base para o cálculo do fatorial
num = int(input("Digite um número fatorial: "))
# Inicializa a variável acumuladora do resultado com 1 (elemento neutro da multiplicação)
fatorial = 1 

# Validações matemáticas básicas do cálculo de fatorial
if num < 0:
    print("Esse número não possui fatorial (números negativos)")
elif num == 0:
    print("O fatorial de 0 é 1")
else:
    # O laço roda de 1 até o próprio número informado (num + 1 para incluí-lo)
    for i in range(1, num + 1):
        # Multiplica o valor acumulador atual pelo próximo número da sequência
        fatorial = fatorial * i
    # Exibe o produto final totalizado
    print(f"O fatorial de {num} é {fatorial}")
```

### Exercício 8: Operações com Listas
- **Funcionamento:** Demonstra o uso de funções embutidas do Python (len, max, min, sum, sorted) para extrair métricas e ordenar uma lista numérica pré-definida.

```python
# Define a lista original contendo valores numéricos inteiros desordenados
L = [5, 7, 2, 9, 4, 1, 3]

# a) A função len() conta e retorna a quantidade de itens na lista
tamanho = len(L)
print(f"a) Tamanho da lista: {tamanho}")

# b) A função max() varre a lista e extrai o maior valor numérico dela
maior = max(L)
print(f"b) Maior valor: {maior}")

# c) A função min() varre a lista e extrai o menor valor numérico dela (Correção: adicionado print)
menor = min(L)
print(f"c) Menor valor: {menor}")

# d) A função sum() soma de maneira agregada todos os itens da lista (Correção: texto do print ajustado)
soma = sum(L)
print(f"d) Soma de todos os elementos: {soma}")

# e) sorted() organiza os itens do menor para o maior e gera uma nova lista (Correção: removido reverse)
crescente = sorted(L)
print(f"e) Lista em ordem crescente: {crescente}")

# f) Usar sorted() com o parâmetro reverse=True gera a lista de trás para frente (Correção: adicionado item f)
decrescente = sorted(L, reverse=True)
print(f"f) Lista em ordem decrescente: {decrescente}")
```

### Exercício 9: Dicionário de Lanchonete
- **Funcionamento:** Demonstra a criação de uma estrutura de chaves e valores (Key-Value). O dicionário indexa o nome do produto como identificador associado ao seu valor decimal (float).

```python
# Declaração do dicionário lanchonete mapeando strings (chaves/produtos) para floats (valores/preços)
lanchonete = {
    "salgado": 4.50,
    "Lanche": 6.50,
    "Suco": 3.00,
    "Refrigerante": 3.50,
    "Doce": 1.00
}

# Imprime o dicionário completo estruturado no console
print(lanchonete)
```

### Exercício 10: Validação de Senha
- **Funcionamento:** Algoritmo de controle de acesso que prende a execução dentro de um bloco while até que o texto inserido seja exatamente igual à senha numérica cadastrada.

```python
# Define a senha mestra correta em formato string (texto)
senha_correta = "676767"

# Inicializa uma variável vazia para armazenar as futuras tentativas do usuário
senha_digitada = ""

# O bloco continuará repetindo enquanto o texto digitado for DIFERENTE da senha mestra
while senha_digitada != senha_correta:
    # Solicita a digitação da senha no console
    senha_digitada = input("Digite a senha: ")
    
    # Se a senha estiver incorreta, emite o alerta visual antes de reiniciar o loop
    if senha_digitada != senha_correta:
        print("Senha incorreta! Tente novamente")

# Esta linha só será executada se a condição do 'while' falhar (ou seja, quando forem iguais)
print("Acesso liberado")
```

### Exercício 11: Tabuada de um Número (1 a 10)
- **Funcionamento:** Solicita ao usuário um número inteiro entre 1 e 10. O programa valida se o número inserido está dentro deste intervalo e, se válido, utiliza um laço for com a função range(1, 11) para gerar e imprimir todas as multiplicações de 1 a 10, construindo a tabuada completa.

```python
# Solicita um número ao usuário e o converte de texto (string) para inteiro (int)
num = int(input("Digite um número de 1 a 10 para ver a tabuada: "))

# Estrutura condicional para validar se o número está fora do intervalo de 1 a 10
if num < 1 or num > 10:
    # Caso esteja fora do intervalo, exibe uma mensagem de erro na tela
    print("Número errado! Digite apenas o número de 1 a 10")
else:
    # Caso o número seja válido, inicia a exibição da tabuada
    print(f"Tabuada do {num}:")
    # Laço de repetição que vai de 1 até 10 (o 11 indica o limite superior exclusivo)
    for i in range(1, 11):
        # Calcula o produto multiplicando o número fornecido pelo multiplicador atual (i)
        resultado = num * i
        # Exibe o resultado formatado de forma organizada (ex: 5 x 1 = 5)
        print(f"{num} x {i} = {resultado}")
```
