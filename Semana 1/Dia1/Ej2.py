while True:
    numero = int(input("Introduce un número entero mayor que 1: "))
    if numero > 1:
      break
    print("El número debe ser mayor que 1.")

def es_primo(n):
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

if es_primo(numero):
  print(f"El número {numero} es primo.")
else:
  print(f"El número {numero} no es primo.")

primos = []
for i in range(2, numero + 1):
    if es_primo(i):
        primos.append(i)
print(f"Los números primos hasta el {numero} son:")
print(primos)