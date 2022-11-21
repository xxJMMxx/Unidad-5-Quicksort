# El primer método a implementar es el quick_sort que recibe una lista, un índice de inicio y final,
# lo que hace es poner una condición mediante un if que se pregunta si el índice de inicio es mayor que
# el índice final, si es así ejecuta el método partición y luego se llama así mismo recursivamente, pero
# con nuevos datos de entrada, esto para ordenar las nuevas sublistas que se van a crear, una para la sublista
# izquierda y otra para la sublista derecha.
def quick_sort(lista, inicio, final):
    if inicio < final:
        pivote_indice = particion(lista, inicio, final)

        # Llamar quick_sort de inicio al pivote, y de pivote + 1 a final
        quick_sort(lista, inicio, pivote_indice - 1)
        quick_sort(lista, pivote_indice + 1, final)


# En este método recibe datos de entrada desde el método quick_sort, lo primero que hace es elegir el elemento
# pivote, para este caso se eligió el elemento final de la lista. Se utiliza un ciclo for para iterar la lista
# con un rango que va desde el valor en la variable inicio hasta el valor en la variable final. Dentro del ciclo
# for hay un condicional if, cuando el elemento que se está iterando(j) sea menor que el pivote, se cambiaran de
# posición con el elemento en la posición de la variable uni, a la vez se incrementa en 1 el valor de la variable
# uni. Lo siguiente que se hace es intercambiar el pivote por el último elemento que esté en la posición de la
# variable uni, este ciclo se hace cada vez
def particion(lista, inicio, final):
    pivote = lista[final]
    ini = inicio

    for j in range(inicio, final):
        # Menores= izquierda
        if lista[j] < pivote:
            lista[ini], lista[j] = lista[j], lista[ini]
            ini += 1
    # Mover pivote a su posición correspondiente
    pivot_index = ini
    lista[pivot_index], lista[final] = lista[final], lista[pivot_index]
    return pivot_index


# instancia y datos de la lista que sera ordenada
lista = [5, 3, 1, 2, 6, 4, 4, 5, 9, 2, 3, 34, 32, 90, 10000]
inicio = 0
final = len(lista) - 1

print("Lista original: ")
print(lista)

quick_sort(lista, inicio, final)
print("Lista ordenada: ")
print(lista)
