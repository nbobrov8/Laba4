#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    n = int(input("Введите количество экзаменов "))

    if n == 1:
        print('Мы успешно сдали', n, "экзамен")
    elif n == 2 or n == 3 or n == 4:
        print('Мы успешно сдали', n, "экзамена")
    elif n == 5 or n == 6 or n == 7 or n == 8 or n == 9 or n == 10 or n == 11 or n == 12 or n == 13 \
            or n == 14 or n == 15 or n == 16 or n == 17 or n == 18 or n == 19 or n == 20:
        print("Мы успешно сдали", n, "экзаменов")
    else:
        print("Число N не входит в диапозон от 1 до 20", file=sys.stderr)
        exit(1)