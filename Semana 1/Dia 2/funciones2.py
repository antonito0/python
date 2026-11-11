def es_primo(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primos_hasta(n):
    primos = []
    for i in range(2, n + 1):
        if es_primo(i):
            primos.append(i)
    return primos