from funciones2 import es_primo, primos_hasta

while True:
    numero = int(input("Introduce un número entero mayor que 1: "))
    if numero > 1:
      break
    print("El número debe ser mayor que 1.")

if es_primo(numero):
  print(f"El número {numero} es primo.")
else:
  print(f"El número {numero} no es primo.")

print(f"Los números primos hasta el {numero} son:")
for i in primos_hasta(numero):
   print(i)