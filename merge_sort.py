import random

def merge_sort(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]

        print(izquierda, '*' * 3, derecha)
        print('-'*10)
#Recursive call
        merge_sort(izquierda)
        merge_sort(derecha)

#Sublist iterators
        i = 0
        j = 0
#Principal list iterator
        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else: 
                lista[k] = derecha[j]
                j += 1
            
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
        
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

    return lista


def run():
    length = int(input('De que tamaño va a ser la lista a ordenar?: '))
    lista = [random.randint(1, 100) for i in range(length)]

    print(lista)

    lista_ordenada = merge_sort(lista)

    print(lista_ordenada)


if __name__ == '__main__':
    run()