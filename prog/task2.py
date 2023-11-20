#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    a = input("Введите первую строку ")

    b = input("Введите вторую строку ")

    print(set(a).intersection(set(b)))