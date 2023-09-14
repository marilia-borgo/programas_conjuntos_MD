def tabela_verdade(operador):
  tabela = {}
  if operador == "and":
    for x in (True, False):
      for y in (True, False):
        tabela[(x, y)] = x and y
  elif operador == "or":
    for x in (True, False):
      for y in (True, False):
        tabela[(x, y)] = x or y

  else:
    raise ValueError("Operador não válido")
  return tabela


print("tabela verdade e ")
print(tabela_verdade("and"))
print("--------------------------")

print("tabela verdade ou")
print(tabela_verdade("or"))
print("--------------------------")
