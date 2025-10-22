from random import *
def selectsort(x):
    for i in range(len(x)):
        for j in range(len(x)-i-1):
            if x[j]>x[j+1]:
                x[j+1],x[j]=x[j],x[j+1]
x=[randint(1,100) for _ in range(10)]
print(x)
selectsort(x)
print(x)

##再编一个冒泡排序法
