m1 = ((2,3,5),(7,2,4))
m2 = ((1,6),(7,2),(0,5))

def p(m): #Esta función nos determina cuantas columnas tiene la matriz y nos devuelve un número entero
    fila = m[0]
    a = enumerate(fila)
    # a nos da el número de elementos que tiene "fila" que es el primer elemento de la lista (matriz) m.
    return a
    # se podría poner --> return enumerate(m[0]) para dejarlo en una línea

#Esta función nos determina si podemos o no multiplicar 2 matrices que le damos como argumentos
def can_or_cant(a1,a2):
    #Creamos dos variables llamadas "longitud" para saber la estructura de la función
    longitud1 = [len(a1),p(a1)]
    longitud2 = [len(a2),p(a2)]
    #El primer elemento de la lista son el número de filas que tiene la matriz, es decir, la longitud de la matriz
    #El segundo elemento de la lista, en la que llamamos a la función "p()", nos da el número de columnas, es decir,
    #los elementos de cada elemento que integra la lista
    if longitud1[1] == longitud2[0]:
        return True
    # ponemos return True/False para no tener que modificar en un futuro esto en mas de un sitio
    else:
        return False
    #Si el número de columnas de una matriz coincide con el número de filas de la otra matriz, se puede multiplicar

can_or_cant(m1,m2)
