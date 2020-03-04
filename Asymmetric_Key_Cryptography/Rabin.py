import math
import random

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

m = int(input("Enter Plain Text : "))
p = int(input("Enter p : "))
q = int(input("Enter q : "))

n = p*q

c=(m**2)%n

print('Cipher text = '+str(c))

mp = (c**((p+1)//4))%p
mq = (c**((q+1)//4))%q

gcd, yp, yq = egcd(p, q)

r1 = (yp*p*mq + yq*q*mp)%n
r2 = n-r1
r3 = (yp*p*mq - yq*q*mp)%n
r4 = n-r3

print('DeCipher text : ')

print(r1, r2, r3, r4)