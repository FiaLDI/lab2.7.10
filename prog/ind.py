#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    A = {"b","d","l","p"}
    B = {"b", "d", "e", "l", "p", "x"}
    C = {"k", "l", "p", "t"}
    D = {"d", "k", "o", "p", "q", "u", "v"}

    U = A.union(B).union(C).union(D)

    nB = U.difference(B)

    X = (A.difference(B)).intersection(C.union(D))

    Y = (A.intersection(nB)).union(C.difference(D))

    print(f"X = {X}, Y = {Y}")
