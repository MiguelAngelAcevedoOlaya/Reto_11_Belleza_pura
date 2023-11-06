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
  
  for l in range(len(matriz)): # Recorre fila
    sum_fil = 0
    for m in range(len(matriz[i])): # Recorre cada elemento de la fila
      sum_fil = sum_fil + matriz[l][m] # Va sumando los elementos de cada fila
    print("La suma de la fila " +str(l+1)+ " es: " +str(sum_fil)) 

if __name__ == "__main__":
  fil = int(input("Agrega el número de filas: ")) # Fila
  col = int(input("Agrega el número de columnas: ")) # Columna
  sum_matric(fil,col)