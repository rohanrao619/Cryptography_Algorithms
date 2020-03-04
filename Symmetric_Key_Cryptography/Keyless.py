# Keyless 
plain=input('Enter Plain text : ')
n=int(input('Enter no. of rows : '))
cipher=''
decipher=''
for i in range(n):
    x=0
    while (i+(x*n))<len(plain):
        cipher+=(plain[i+(x*n)])
        x+=1
print('Ciphered Text is : '+cipher)   

for i in range(len(cipher)//n):
    x=0
    while (i+x*(len(cipher)//n))<len(cipher):
        if(len(cipher)%n!=0 and x!=0 and (i+x*(len(cipher)//n)+1)<len(cipher)):
           decipher+=cipher[i+x*(len(cipher)//n)+1] 
        else:
            decipher+=cipher[i+x*(len(cipher)//n)]
        x+=1
           
print('DeCiphered Text is : '+decipher)