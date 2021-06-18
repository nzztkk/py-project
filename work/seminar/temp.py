# import os
# os.chdir('C:\lessons\проектный семинар по python\work')

# S = "А роза упала на Азора"
# l1 =  [x+1 for x in range(10)]
# l2 = [x*10 for x in range(10)]
# for i in range(10):
#     if l1[i]%2 == 0:
#         l1[i]*=2
        
#  param = [float (s) for s in input("Введите три числа через пробел: ").split()]


# S1 = S.split('а')
# S2 = S.split()
# S3 = ' '.join(S2)
# S4 = ' '.join(S2[-2:-4:-1])

# l11 = sorted(l1)
# S22 = sorted(S2)

# 'апельсин' < 'ананас'

# names = [('Ann', 8, 4.5, 9), ('Ann', 6, 7, 10), ('Dan', 9, 8, 9)] 
# nam1 = sorted(names)

# for i in range (1, len(12), 2):12[i] *=2 

# 14.sort()
# 16 = sorted(12)

import os
os.disk("C:\lessons\проектный семинар по python\work")

def func (a,b,c): return a+b+c
func(2,4,6)
f = lambda a,b,c: a+b+c
f(2,4,6)

z = ['one','two','five']
f1 = lambda x:x[1]
print(list(map(f1,z)))

lowest = (lambda x,y:if x<y else y)
lowest('apple','pie')

def action(x):
    return(lambda y,z1:x*y+z1)
act = action(10)
act2 = act(5)
act2(5)

action1 = (lambda y:(lambda x: x*y) )
act1 = action(20)
act1(2)
