
def exponencial():
  exponentes = []
  for x in range(2):
    b = int(input("Ingrese un número base: "))
    e = int(input("Ingrese un número exponente: "))
    exp = b**e
    print(b, "elevado a la", e, "es", exp)
    print()
    exponentes.append(exp)
    
  mayor = max(exponentes)
  print("El mayor de los resultados fue:",mayor)
  
exponencial()
