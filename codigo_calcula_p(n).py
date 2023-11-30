
def fatorial(n):
    if(n==0):
        return 1
    else:
      '''
      utiliza-se aqui a definicao indutiva para o calulo de p(n)
      '''
      return n*fatorial(n-1)