import numpy as np
from numpy import linalg,matrix
import numpy

def modInv(a,p):          
  for i in range(1,p):
    if (i*a)%p==1:
      return i
  return False


def minor(A,i,j):    
  A=numpy.array(A)
  minor=numpy.zeros(shape=(len(A)-1,len(A)-1))
  p=0
  for s in range(0,len(minor)):
    if p==i:
      p=p+1
    q=0
    for t in range(0,len(minor)):
      if q==j:
        q=q+1
      minor[s][t]=A[p][q]
      q=q+1
    p=p+1
  return minor

def modMatInv(A,p):       
  n=len(A)
  A=matrix(A)
  adj=numpy.zeros(shape=(n,n))
  for i in range(0,n):
    for j in range(0,n):
      adj[i][j]=((-1)**(i+j)*int(round(linalg.det(minor(A,j,i)))))%p
  return (modInv(int(round(linalg.det(A))),p)*adj)%p


def encryption(plain_text,key_f = None):
	plain_text = plain_text.lower()
	N = len(plain_text)
	arr = np.zeros((N,1))
	for i,ch in enumerate(plain_text):
		arr[i,0] = ord(ch)-ord('a')
	key = np.random.randint(0,25,(N,N))
	while modMatInv(key,26).any()==False:
		key = np.random.randint(0,25,(N,N))
	# print(linalg.det(key))
	if key_f is not None:
		key = key_f
	cipher = np.matmul(key,arr)
	cipher = cipher%26
	cipher_text = ''
	for i in cipher:
		cipher_text += chr(i+ord('a'))
	return cipher_text,key

def decryption(cipher_text,key):
	cipher_text = cipher_text.lower()
	N = len(cipher_text)
	arr = np.zeros((N,1))
	for i,ch in enumerate(cipher_text):
		arr[i,0] = ord(ch)-ord('a')
	key_inv = modMatInv(key,26)
	print("Inverse Key:\n",key_inv)
	plain = np.matmul(key_inv,arr)
	plain = plain%26
	plain_text = ''
	for i in plain:
		plain_text += chr(i+ord('a')) 
	return plain_text

plain_text = str(input("Enter Plain Text : "))
# key = np.array()
cipher,key = encryption(plain_text)
print('Cipher Text : {}'.format(cipher))
print('Key:\n',key)
print('DeCiphered Text : ',decryption(cipher,key))