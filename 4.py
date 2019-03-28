def primos_hermanos():
  n = int(input("Ingrese un número "))
  div = 0
  
  if n%6 == 0:
    print(n,"NO es primo hermano")
  else:
    for x in range (1,n+2):
      if ((n+1)%x) == 0:
        div = div + 1
    if div<=2:
      print(n,"ES primo hermano")
    else:
      print(n,"NO es primo hermano")
primos_hermanos()