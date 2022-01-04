import random

def insertion_sort(list):
    for i in range(1, len(list)):
        actual_value = list[i]
        current_position = i

        while list[current_position - 1] > actual_value and current_position > 0:
            list[current_position] = list[current_position - 1]
            current_position -= 1

            list[current_position] = actual_value
    
    return list


def run():
    long = int(input('Ingresa la longitud de la lista a ordenar: '))

    my_list = [random.randint(0, 100) for i in range(long)]
    print(my_list)

    my_ordered_list = insertion_sort(my_list)
    print(my_ordered_list)


if __name__ == '__main__':
    run()