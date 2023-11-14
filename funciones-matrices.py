m1 = ((2,3,5),(7,2,4))
m2 = ((1,6),(7,2),(0,5))
#Esta función nos determina cuantas columnas tiene la matriz y nos devuelve un número entero
def p(m):
    fila = m[0]
    a = enumerate(fila)
    # a nos da el numero de elementos que tiene "fila" que es el primer elemento de la lsita (matriz) m.
    return a
    # se podría poner --> return enumerate(m[0]) para dejarlo en una línea

#Esta función nos determina si podemos o no multiplicar 2 matrices que le damos como argumentos
def can_or_cant(a1,a2):
#Creamos dos variables llamadas "longitud" para saber la estructura de la función
    longitud1 = [len(a1),p(a1)]
    longitud2 = [len(a2),p(a2)]
#El primer elemento de la lista son el número de filas que tiene la matriz, es decir, la longitud de la tupla (matriz)
#El segundo elemento de la lista, en la que llamamos a la función "p()", nos da el número de columnas, es decir,
#los elementos de cada elemento que integra la tupla
    if longitud1[1] == longitud2[0]:
        print(f"CAN")
    else:
        print(f"CANNOT")
#Si el número de columnas de una matriz coincide con el número de filas de la otra matriz, se puede multiplicar

can_or_cant(m1,m2)