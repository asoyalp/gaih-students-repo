# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WmYhROM-LMxPqRDZev69FbRRZ3GtIw9e
"""

cv1 = {"Name" : "Altay", "Surname" : "Soyalp", "Age" : 32, "Gender" : "Male", "Education" : "Boğaziçi University"}
cv2 = {"Name" : "Mehmet", "Surname" : "Soyalp", "Age" : 70 , "Gender" : "Male", "Education" : "Midle East Technical University"}
cv3 = {"Name" : "Aybike", "Surname" : "Aktürk Soyalp", "Age" : 29, "Gender" : "Female", "Education" : "Muğla University"}
cv4 = {"Name" : "Tülin", "Surname" : "Aktürk", "Age" : 52 , "Gender" : "Female", "Education" : "Gazi University"}
cv5 = {"Name" : "Mustafa", "Surname" : "Aktürk", "Age" : 62, "Gender" : "Male", "Education" : "Bursa Uludağ University"}

cvs = [cv1,cv2,cv3,cv4,cv5]

print(*cvs, sep="\n")

print(cv1.keys())

print(cv1.values())
print(cv2.values())
print(cv3.values())
print(cv4.values())
print(cv5.values())