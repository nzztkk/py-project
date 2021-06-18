# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 19:57:33 2021

@author: nurkh
"""

import os
import matplotlib.pyplot as plt
import numpy as np


os.chdir("C:\lessons\проектный семинар по python\work")



def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

#t1= np.arange(0,5.05,0.1)
#t2= np.arange(0,5.01,0.02)
    
#plt.figure(1)
#plt.subplot(121)
#plt.plot(t1,f(t1),'ro', t2,f(t2),'k')
#plt.axis([0,4,-1.1,1.1])
#plt.title("It's not easy as 1,2,3")

#plt.subplot(122)
#plt.plot(t2,np.cos(2*np.pi*t2),'g--')
#plt.title("Easy as 1,2,3")
#plt.axis([0,4,-1.1,1.1])

plt.show()
plt.plot(t2,np.cos(2*np.pi*t2),'g--')
plt.xlabel('x')
plt.ylabel('$y=cos(2*\pi*x)$')
#plt.text(4,1.1, r'$\pi=3.14...$')
plt.annotate('locale max' , xy = (2,1), xytext = (3,1.5),
             arrowprops=dict(facecolor'red' , shrink = ))
plt.axis([0,5,-1.1,2])
plt.show()
