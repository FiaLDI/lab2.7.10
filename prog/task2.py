#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    first_string = input("Введите первую строку ")
    second_string = input("Введите вторую строку ")

    common_syms = set(first_string).intersection(set(second_string))

    print(common_syms)