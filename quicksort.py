# -*- coding: utf-8 -*-

def sort(array):
    #Сортировка массива с помощью quicksort. средняя сложность алгоритма O(n*log n)
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return sort(less)+equal+sort(greater)  
    else:
        return array

if __name__ == "__main__":
    pass