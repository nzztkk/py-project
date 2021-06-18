# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 21:22:42 2021

@author: nurkh
"""

import os
os.chdir("C:\lessons\проектный семинар по python\work")


# SLOVARI #

students = ["Anya","Kolya","Vasya","Petya"]
grades = [5,4,2,4,]


gradebook = {"Anya":5,"Kolya":4,"Vasya":2,"Petya":4,}
gradebook ['Vasya']
gradebook ['Kira'] = 3

new_sum = {(1,5):'six', "tree":15}
new_sum = ["tree"]

gradebook.keys()
gradebook.values()


for k in gradebook:
    print(k, gradebook [k])
    
for k,v in gradebook.items():
    if v==4: print(k)
    
new_grade=dict(zip(students,grades))

new_grade ['Vasya'] = 5

### test base


    