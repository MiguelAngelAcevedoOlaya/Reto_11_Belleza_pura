def sum_matric(fil: int, col: int)-> int:
  # Crear la matriz
  filas = []
  matriz = [] # Matriz A
  filas_b = []
  matriz_b = [] # Matriz B
  for i in range(fil): # Recorre filas
    for j in range(col): # Recorre cada elemento de la fila
      num = float(input("Agrega un número a matriz A: ")) # Agrega número para cada fila de matriz A
      num_b = float(input("Agrega un número a matriz B: ")) # Agrega número para cada fila de matriz B
      filas.append(num)
      filas_b.append(num_b)
    matriz.append(filas) 
    matriz_b.append(filas_b)
    filas = [] # Se crea la matriz A y B
    filas_b = []
  print("Matriz A: ")
  for h in range(len(matriz)):
    print(matriz[h]) # Imprimir bonito matriz A
  print("Matriz B: ")
  for k in range(len(matriz_b)):
    print(matriz_b[k]) # Imprimir bonito matriz B

  matriz_c = [] # Matriz C
  fila_c = []
  for n in range (fil):
      for o in range (col):
          fila_c.append(0) # Agregamos solo 0 a la matriz, del mismo número de filas y columnas
      matriz_c.append(fila_c)
      fila_c = []

  for l in range(fil):
      for m in range(col):
          matriz_c[l][m] = matriz[l][m] + matriz_b[l][m] #Sumamos los valores de cada matriz al recorrer cada dato, y cambiando el valor anterior de la matriz c a la suma del valor de las matrices a y b
  print("La suma de las dos matrices es: ")
  for p in range(len(matriz_c)):
    print(matriz_c[p]) # Imprimir bonito matriz C
    
if __name__ == "__main__":
  fil = int(input("Agrega el número de filas: ")) # Fila
  col = int(input("Agrega el número de columnas: ")) # Columna
  sum_matric(fil,col)