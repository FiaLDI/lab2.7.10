#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    a = input("Введите строку ")

    k = 0

    s = set("ауоыиэяюёе")
    
    for i in a:
        if i in s:
            k += 1
    print("Количество гласных:", k)