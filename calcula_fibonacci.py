'''
Utiliza-se o conceito de induçao finita para o calculo
da seguencia de fibonacci ate x numero
'''

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fib_sequence = [fibonacci(i) for i in range(19)])