import numpy as np

p = int(input(' Enter P : ')) 
q = int(input(' Enter Q : ')) 
plain = int(input(' Enter Plain Text : ')) 

n = p*q 

t = (p-1)*(q-1) 

for e in range(2,t): 
	if np.gcd(e,t)== 1: 
		break

flag=0
i=1 

while flag==0 :
  
  if (i*e)%t==1:
    flag=1
  else :
    i+=1

d=i    

print(' Public Key e = '+str(e))
print(' Private Key d = '+str(d))
   
cipher = (plain**e)%n

decipher = (cipher**d)%n

print(' Encrypted (Cipher) Text : '+str(cipher))
print(' Decrypted (DeCipher) Text : '+str(decipher))