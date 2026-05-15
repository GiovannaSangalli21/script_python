n = int(input("Até qual termo você quer gerar? "))

a, b = 0, 1  # Começamos com 0 e 1
sequencia = []

for _ in range(n):
    sequencia.append(a)
    a, b = b, a + b  # O novo 'a' vira o antigo 'b', e o novo 'b' vira a soma dos dois

print(f"Série de Fibonacci: {sequencia}")