def potencia(base, exp=2):
    if exp < 0:
        return 1 / potencia(base, -exp)

    resultado = 1
    for _ in range(exp):
        resultado *= base
    return resultado


def factorial(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")

    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado