# Reto 11

## Punto 1

### Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

Para este punto en primer lugar creamos la matriz A y B, dando la libertad al usuario de elegir el número de filas y columnas, teniendo en cuenta que sera el mismo para ambas matrices. Este codigo es en base a lo que aprendimos en clase, se crea la lista de la fila, esta se agrega a la matriz, luego se limpia para poder introducer los siguientes valores de la fila hasta que se cumpla el número de columnas..

Posterior a eso creamos una matriz con la mismas filas y columnas, de la A y B, y le añadiremos unicamente 0, esto para luego poder agregar los valores que necesitamos para volver esta matriz la suma de las dos primeras.

Esblecemos un codigo for de columnas y filas para que recorra cada valor de las tres matrices, en el que el valor de la tercera matriz, sera igual a la suma de los dos primeras. Modificando todos los valores de la lista C y tranformandola en la suma de cada valor de la A y la B.

Utilizamos el ciclo for para imprimir todas las matrices de forma bonita.

```
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
```

## Punto 2

### Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

Para este punto en primer lugar creamos la matriz A y B, dando la libertad al usuario de elegir el número de filas y columnas, teniendo en cuenta que sera el mismo para ambas matrices. Este codigo es en base a lo que aprendimos en clase, se crea la lista de la fila, esta se agrega a la matriz, luego se limpia para poder introducer los siguientes valores de la fila hasta que se cumpla el número de columnas..

Posterior a eso creamos una matriz con la mismas filas y columnas, de la A y B, y le añadiremos unicamente 0, esto para luego poder agregar los valores que necesitamos para volver esta matriz la multiplicación de las dos primeras.

Esblecemos un codigo for de columnas y filas para que recorra cada valor de las tres matrices, en el que el valor de la tercera matriz, sera igual a la multiplicación de los dos primeras. Modificando todos los valores de la lista C y tranformandola en la multipliación de cada valor de la A y la B.

Utilizamos el ciclo for para imprimir todas las matrices de forma bonita.

```
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
            matriz_c[l][m] = matriz[l][m] * matriz_b[l][m] #Multiplicamos los valores de cada matriz al recorrer cada dato, y cambiando el valor anterior de la matriz c a la multiplicación del valor de las matrices a y b
    print("La suma de las dos matrices es: ")
    for p in range(len(matriz_c)):
        print(matriz_c[p]) # Imprimir bonito matriz C

if __name__ == "__main__":
  fil = int(input("Agrega el número de filas: ")) # Fila
  col = int(input("Agrega el número de columnas: ")) # Columna
  sum_matric(fil,col)
```

## Punto 3

### Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.

En primer lugar creamos la matriz de la misma manera que las creamos en los puntos anteriores.

Ahora creamos otra matriz, que será la matriz transpuesta de la primera matriz, en la que invertimos las filas y las columnas de la primera, ej: si la matriz a tiene 2 filas y 3 columnas. La matriz transpuesta tendra 3 filas y 2 columnas.

Usamos un codigo parecido al que se uso para sumas dos matrices y agregarla en la tercera, pero en esta utlizamos el codigo for de columna con fila, invertido para que los valores de las matrices queden invertidos, Dandonos una matriz transpuesta, con los mimos valores pero sus columnas siendo las filas de la matriz original, y sus filas siendo las columnas.

Tambíen utilizamos el codigo para imprimirlas de forma bonita.

```
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
```
## Punto 4

### Desarrollar un programa que sume los elementos de una columna dada de una matriz

Para este punto al igual que los puntos anterior utilizamos el codigo para generar la matriz.

Utilizamos los codigos que se usaron en clase para recorrer las matrices, pero en ves de ser primero recorrer cada fila, esta primero seleccionara una columna, y sumara los datos de la primera fila, imprimiendo este valor y el valor de la columna al que pertenece, luego continuara con la siguiente columna y asi infinitamente hasta que se acaben las columnas.

```
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
```

## Punto 5

### Desarrollar un programa que sume los elementos de una fila dada de una matriz.

Utilizamos el mismo codigo que el anterior, pero unicamente intercambiando los valores en el ultimo codigo ya que no tomata las columnas, sino cada fila y sumara todos los valores que se encuentren en esta, imprimiendo el valor. Asi infinitamente hasta que se acaben las filas

```
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
```


