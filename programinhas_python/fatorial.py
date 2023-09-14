"""
Programa que calcula a fatorial de um número
A noção de conjuntos é utilizada aqui pois utilizamos o conjunto
de números naturais iguais ou menos que o número inserido.
podendo ser representado pelo conjunto:  n = {0,1, ..., n}
"""


def fatorial(n):
  if n == 0:
    return 1
  else:
    return n * fatorial(n - 1)


if __name__ == "__main__":
  n = int(input("Digite um número natural: ")) #aqui estamos utilizando o conjunto dos números naturais 
  print(f"O fatorial de {n} é {fatorial(n)}")