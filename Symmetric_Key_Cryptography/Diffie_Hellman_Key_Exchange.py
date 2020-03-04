import numpy as np

n=int(input('Enter large prime N : '))
g=int(input('Enter large prime G : '))

x=1+int(10000*np.random.rand())
y=1+int(10000*np.random.rand())

print('X and Y = '+str(x)+','+str(y))

a=(g**x)%n
b=(g**y)%n

print('A and B = '+str(a)+','+str(b))

k1=(b**x)%n
k2=(a**y)%n

print('k1 and k2 = '+str(k1)+','+str(k2))

print('k1 == k2 Key Exchanged !')