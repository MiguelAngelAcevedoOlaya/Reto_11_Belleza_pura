def sum_matric(fil: int, col: int)-> int:
  # Crear la matriz
  filas = []
  matriz = []
  for i in range(fil): # Recorre filas
    for j in range(col): # Recorre cada elemento de la fila
      num = int(input("Agrega un número: ")) # Agrega número para cada fila 
      filas.append(num)
    matriz.append(filas) 
    filas = []   # Se crea la matriz
  for h in range(len(matriz)):
    print(matriz[h]) # Imprimir bonito
  
  for m in range(len(matriz[i])): # Recorre cada elemento de la fila
    sum_col = 0
    for l in range(len(matriz)): # Recorre fila
      sum_col = sum_col + matriz[l][m] # Va sumando los elementos de cada columna
    print("La suma de la columna " +str(m+1)+ " es: " +str(sum_col)) 

if __name__ == "__main__":
  fil = int(input("Agrega el número de filas: ")) # Fila
  col = int(input("Agrega el número de columnas: ")) # Columna
  sum_matric(fil,col)