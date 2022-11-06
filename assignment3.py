#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def insert_space(n, k):
    return n[:k] + " " + n[k:]


def split_method(n):
    a = n.replace("()", "")
    a = a.replace("S;M;", "")
    j = 0
    for i in a:
        if i.isupper() == True:
            a = insert_space(a, j)
            j += 1
        j += 1
    return a.lower()


def split_class(n):
    a = n.replace("S;C;", "")
    j = 0
    for i in a:
        if i.isupper() == True:
            a = insert_space(a, j)
            j += 1
        j += 1
    return a[1:].lower()


def split_variable(n):
    a = n.replace("S;V;", "")
    j = 0
    for i in a:
        if i.isupper() == True:
            a = insert_space(a, j)
            j += 1
        j += 1
    return a.lower()


def remove_space(n, k):
    a = n
    h = a[k+1].upper()
    a = a[:k+1] + a[k+2:]
    a = a[:k+1] + h + a[k+1:]
    return a


def combine_method(n):
    a = n.replace("C;M;", "")
    j = 0
    for i in a:
        if i == " ":
            a = remove_space(a, j)
        j += 1
    return a.replace(" ", "") + "()"


def combine_class(n):
    a = n.replace("C;C;", "")
    j = 0
    for i in a:
        if i == " ":
            a = remove_space(a, j)
        j += 1

    h = a[0].upper()
    a = a[:0] + a[1:]
    a = a[:0] + h + a[0:]

    return a.replace(" ", "")


def combine_variable(n):
    a = n.replace("C;V;", "")
    j = 0
    for i in a:
        if i == " ":
            a = remove_space(a, j)
        j += 1

    return a.replace(" ", "")
