'''
Nesse codigo utiliza-se de inducao finita, propondo 
que se n é primo para um certo valor de n, 
então n é primo para todo valor de n maior ou igual a n.
'''


def verifica_primo(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

print(verifica_primo(13))
print(verifica_primo(15))

