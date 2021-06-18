# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 19:44:59 2021

@author: nurkh
"""
import os
os.chdir("C:\lessons\проектный семинар по python\work")

import numpy as np

D = np.array([1,2,3,4,5])
D.shape(5,)
D.ndim

D1 = np.array ([[1,2,3], [5.5,6.5,7.5]])
D1.shape = (3,2)
D1.ndim
print ('dim:%i shape:(%i,%i) type: $s'
       %(D1.ndim, D1.shape[0], D1.shape[1], D1.dtype))

q = np.array([1,20,3,4])
w = np.array([9,80,7,60])
#q+w
q1 = np.concatenate([q,w])
q1.shape = (4,2)

q2 = q1.copy()

y = q1[q1>10]
q1[(q1<60)&(q1>2)]
z=q1[(q1>60)|(q1<2)]


W1 = np.zeros(shape =(3,4),dtype = float)
W2 = np.ones(shape =(2,4),dtype = float)
W3 = np.ones_like(D1)
W4 = np.concatenate([W1,W2])

z1