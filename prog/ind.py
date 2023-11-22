#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    a = {"b","d","l","p"}
    b = {"b", "d", "e", "l", "p", "x"}
    c = {"k", "l", "p", "t"}
    d = {"d", "k", "o", "p", "q", "u", "v"}

    u = a.union(b).union(c).union(d)

    nb = u.difference(b)

    x = (a.difference(b)).intersection(c.union(d))

    y = (a.intersection(nb)).union(c.difference(d))

    print(f"X = {x}, Y = {y}")
