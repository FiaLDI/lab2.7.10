#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    u = set("abcdefghijklmnopqrstuvwxyz")

    a = {"b","d","l","p"}
    b = {"b", "d", "e", "l", "p", "x"}
    c = {"k", "l", "p", "t"}
    d = {"d", "k", "o", "p", "q", "u", "v"}

    bn = u.difference(b)

    x = (a.difference(b)).intersection(c.union(d))

    y = (a.intersection(bn)).union(c.difference(d))

    print(f"X = {x}, Y = {y}")
