# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qszRAUmVS3M3RAVeC4yJ3CJmlZbWgkJQ
"""

list1 = [1,3,5,7,9]
list2 = [2,4,6,8,10]
list1.extend(list2)
list1.sort()
doubles = [i*2 for i in list1]

for i in doubles:
  print(type(doubles))