'''
Função para calcular o fecho reflexivo de uma relação em um conjunto
'''
def fecho_reflexivo(relacao, conjunto):
    fecho = set(relacao)

    for elemento in conjunto:
        par = (elemento, elemento)
        if par not in fecho:
            fecho.add(par)

    return fecho
conjunto = {1, 2, 3}
relacao = {(1, 2), (2, 3)}
fecho_reflexivo = fecho_reflexivo(relacao, conjunto)

print("Fecho reflexivo da relação:", fecho_reflexivo)