# -*- coding: utf-8 -*-


class Cycle_buffer_FIFO():
    def __init__(self, size):
        # size: int -> None
        self._size = size
        self._container = list()

    def __len__(self):
        # -> int
        return self._size

    def __str__(self):
        # -> str
        return str(self._container)

    def _is_full(self):
        # -> bool
        if len(self._container) == self._size:
            return True
        return False

    def append(self, value):
        # value: int -> int or None
        if self._is_full():
            self._container.append(value)
            return self._container.pop(0)
        else:
            self._container.append(value)

    def get(self):
        # -> Any
        return self._container.pop(0)
    
    
class Cycle_buffer_FIFO_child_of_list(list):
    # Альтернативный буфер основанный на структуре list
    def __init__(self, _iterable = []):
        super().__init__(_iterable)
        self._size = 6

    def _is_full(self):
        # Переполнен ли контейнер
        if len(self) >= self._size:
            return True
        return False

    def __add__(self, __x):
        self.append(__x)

    def __sub__(self, __x):
        super().pop(0)

    def append(self, __object):
        # Добавляем в конец буфера объект
        if self._is_full():
            # Если переполнен выгружаем первый элемент
            super().append(__object)
            return super().pop(0)
        return super().append(__object)

    def get(self):
       # Забираем из начала буфера объект
        return super().pop(0)


if __name__ == "__main__":
    pass