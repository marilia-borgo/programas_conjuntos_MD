def intersecao(s1, s2):
  #Retorna a interseção entre dois conjuntos
  return s1 & s2

def uniao(s1, s2):
  #Retorna a união entre dois conjuntos.
  return s1 | s2

def diferenca(s1, s2):
  #Retorna a diferença entre dois conjuntos.
  return s1 - s2

print("intersecção:", intersecao({1,2,3}, {1,2}))
print("união:", uniao({1,2,3}, {1,2}))
print("difereça:", diferenca({1,2,3}, {1,2}))