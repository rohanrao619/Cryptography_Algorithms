plain=input('Enter plain text : ')
cipher=''
decipher=''
key=[]
print('Enter key size : ')
size=int(input())
print('Enter key : ')
for i in range(0,size):
    key.append(int(input()))
if len(plain)%size!=0:
    plain+=('z'*(size-(len(plain)%size)))
for i in range(0,len(plain)//size):
    for j in range(0,size):
        cipher+=plain[(i*size)+key[j]]
print('Ciphered text : '+cipher)
for i in range(0,len(plain)//size):
    for j in range(0,size):
        decipher+=cipher[(i*size)+key.index(j)]
print('DeCiphered text : '+decipher)