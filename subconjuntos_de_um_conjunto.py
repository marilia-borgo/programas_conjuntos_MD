"""
Programinha para gerar todos os subconjuntos possíveis de um
determinado conjunto.
"""


def subconjuntos_conjunto(conjunto : set) -> set:
    subconjunto = []
    if len(conjunto)==0:
        return [[]]
    primeiro_elemento = list(conjunto)[0]
    sub_sem_primeiro_elemento = subconjuntos_conjunto(list(conjunto)[1:])
    for sub in sub_sem_primeiro_elemento:
        subconjunto.append([primeiro_elemento] + sub)
    return sub_sem_primeiro_elemento + subconjunto


print(subconjuntos_conjunto({1,2,3}))