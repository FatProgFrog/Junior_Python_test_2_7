# -*- coding: utf-8 -*-


def isEven(value):
    # value: int -> bool
    return value%2==0


def isEvenAlt(value):
    # value: int -> bool
    checker_list = [str(i) for i in range(0, 10, 2)]
    last_num = str(value)[-1]
    return last_num in checker_list


if __name__ == "__main__":
    pass