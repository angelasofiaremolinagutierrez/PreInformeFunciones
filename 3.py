def primos():
  n = int(input("Ingrese un número "))
  div = 0
  for x in range (1,n+1):
    if (n%x) == 0:
      div = div + 1
    
  if div>2:
    print("El número NO es primo")
  else:
    print("El número ES primo")
  
primos()