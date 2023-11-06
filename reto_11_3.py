def sum_matric(fil: int, col: int)-> int:
    # Crear la matriz
    filas = []
    matriz = []
    for i in range(fil): # Recorre filas
        for j in range(col): # Recorre cada elemento de la fila
            num = float(input("Agrega un número: ")) # Agrega número para cada fila 
            filas.append(num)
        matriz.append(filas) 
        filas = []   # Se crea la matriz
    for h in range(len(matriz)):
        print(matriz[h]) # Imprimir bonito
  
    matriz_t = [] # Matriz transpuesta
    fila_t = []
    for n in range (col):
        for o in range (fil): #Invertimos la fila y la columna a los datos que ingresaron originalmente 
            fila_t.append(0) # Agregamos solo 0 a la matriz, del mismo número de filas y columnas
        matriz_t.append(fila_t)
        fila_t = []
    
    for m in range(len(matriz[i])): # Recorre cada elemento de la fila
        for l in range(len(matriz)): # Recorre fila
            matriz_t[m][l] = matriz[l][m] # Invierte las columnas y las filas
    print("La matriz transpuesta: ") 
  
    for p in range(len(matriz_t)):
        print(matriz_t[p]) # Imprimir bonito

if __name__ == "__main__":
  fil = int(input("Agrega el número de filas: ")) # Fila
  col = int(input("Agrega el número de columnas: ")) # Columna
  sum_matric(fil,col)