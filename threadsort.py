# -*- coding: utf-8 -*-

from threading import Thread
import time


def sleeper(element, rate, received_list):
    #После сна добавляет значение в список.
    time.sleep(element*rate)
    received_list.append(element)

def sort(original_list, rate = 1):
    #Сортировка положительных чисел:
    #скорость не зависит от количества значений в списке,
    #только от значения элемента списка. Элемент списка можно
    #корректировать значением rate. А значит, сложность алгоритма O(1)
    rate = 1/abs(rate)
    received_list = []
    thread_list = []
    for element in original_list:
        Th = Thread(target=sleeper, args=(element, rate, received_list))
        Th.start()
        thread_list.append(Th)

    for thread in thread_list:
        thread.join()
    return received_list


if __name__ == "__main__":
    print("выполняю")
    print(sort([23,54,7,83,2,45,76,2,34,6], 70))