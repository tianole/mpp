##n=int(input('n='))
##s=0
##for i in range(1,n+1):
##    t=1/(4*i-3)-1/(4*i-1)
##    s+=t
##pi=4*s
##print('pi=',pi)
n=int(input('n='))
s=0
i=1
while (1/(4*i-1))>10**(-n):
    t=1/(4*i-3)-1/(4*i-1)
    s+=t
    i+=1
pi=4*s
print('pi=',pi)
    
