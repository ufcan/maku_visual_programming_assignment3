#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import odev3
from os import system

system("clear")

str1 = "S;M;plasticCup()"
str2 = "S;C;LargeSoftwareBook"
str3 = "S;V;pictureFrame"

str4 = "C;M;white sheet of paper"
str5 = "C;C;coffee machine"
str6 = "C;V;mobile phone"

if "S;M;" in str1:
    print(odev3.split_method(str1))

if "S;C;" in str2:
    print(odev3.split_class(str2))

if "S;V;" in str3:
    print(odev3.split_variable(str3))

if "C;M;" in str4:
    print(odev3.combine_method(str4))

if "C;C;" in str5:
    print(odev3.combine_class(str5))

if "C;V;" in str6:
    print(odev3.combine_variable(str6))
