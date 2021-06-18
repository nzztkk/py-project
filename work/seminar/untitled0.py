# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 20:02:11 2021

@author: nurkh
"""

def check(z):
    """
    Проверка аргументов - коэффициентов квадратного уравнения 

    Parameters
    ----------
    z : выражение.

    Returns
    -------
    None.

    """
    if isinstance(z,str):
        return z.isdigit()
    return isinstance(z,(int,float))


check('hhh')

def sqeq(a,b,c):
    """
  Решение квадратного уравнения проверкой 
  коэффициентов и дискриминанта   
  a*x^2 + b*x + c = 0
  Parameters a,b,c
  Returns
  
  корни r1,r2, code
  code = 0 - два корня
  code = 1 - нет корней
  code = 2 - один корень
  code = 3 - ошибка коэффициентов
    -------
    None.
"""
    from math import sqrt
    ### проверка аргумента
    if check(a):
        a = float(a)
    else:
        return(None,None,3)
    if check(b):
        b = float(b)
    else:
        return(None,None,3)
    if check(c):
        c = float(c)
    else:
        return(None,None,3)
    
    #Вычисления 
    if a != 0:
        D = b * b - 4*a*c
        if D>=0:
            r1 = (-b+sqrt(D))/(2*a)
            r2 = (-b+sqrt(D))/(2*a)
            code = 0
        else:
            r1 = None
            r2 = None
            code = 1
            
        return(r1,r2,code)
    return(-c/b, None, 2)

sqeq(0,6,3)


try:
    D = b*b - 4*a*c
    r1=(-b+sqrt(D))/(2*a)
    r2=(-b-sqrt(D))/(2*a)    
except ValueError:
    r1=None
    r2=None
    code=1
except ZeroDivisionError:
    r1=-c/b
    r2=None
    code=2
else:
    pass
finally:
    return (r1,r2,code)

    

