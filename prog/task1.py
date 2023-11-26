#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    input_string = input("Введите строку ")

    count_of_vowels = 0

    vowels = set("ауоыиэяюёе")
    
    for i in input_string.lower():
        if i in vowels:
            count_of_vowels += 1
    print("Количество гласных:", count_of_vowels)