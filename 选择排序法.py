from random import *
def selectsort(x):
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if x[i]>x[j]:
                x[i],x[j]=x[j],x[i]
x=[randint(1,100) for _ in range(10)]
print(x)
selectsort(x)
print(x)
