import numpy as np
j_index = []

def encrypt(new, key):
    x = 0
    cipher = ''
    while((x + 1) < len(new)):
        if(new[x].upper() == 'J'):
        	j_index.append(x)
        	k1 = np.where(key == 'I')
        else:
            k1 = np.where(key == new[x].upper())
        if(new[x + 1].upper() == 'J'):
        	j_indes.append(x + 1)
        	k2 = np.where(key == 'I')
        else:
            k2 = np.where(key == new[x + 1].upper())
        k10 = k1[0][0]  # row
        k11 = k1[1][0]  # column
        k20 = k2[0][0]  # row
        k21 = k2[1][0]  # column
        if(k10 == k20):  # same row
            if(new[x].isupper()):
                cipher += key[k10][(k11 + 1) % 5]
            else:
                cipher += key[k10][(k11 + 1) % 5].lower()

            if(new[x + 1].isupper()):
                cipher += key[k20][(k21 + 1) % 5]
            else:
                cipher += key[k20][(k21 + 1) % 5].lower()

        if(k11 == k21):  # same column
            if(new[x].isupper()):
                cipher += key[(k10 + 1) % 5][k11]
            else:
                cipher += key[(k10 + 1) % 5][k11].lower()
            if(new[x + 1].isupper()):
                cipher += key[(k20 + 1) % 5][k21]
            else:
                cipher += key[(k20 + 1) % 5][k21].lower()

        elif(k10 != k20 and k11 != k21):
            if(new[x].isupper()):
                cipher += key[k10][k21]
            else:
                cipher += key[k10][k21].lower()
            if(new[x + 1].isupper()):
                cipher += key[k20][k11]
            else:
                cipher += key[k20][k11].lower()
        x += 2
    return cipher

def replace_i(i, s):
	if(s[i].isupper()):
		s = s[:i] + 'J' + s[i + 1:]
	else:
		s = s[:i] + 'j' + s[i + 1:]
	return s

def remove_bogus(i, s):
    return s[:i] + s[i+1:]

def decrypt(cipher, key, bogus):
    x = 0
    plain = ''
    while((x + 1) < len(cipher)):
       	k1 = np.where(key == cipher[x].upper())
        k2 = np.where(key == cipher[x + 1].upper())
        k10 = k1[0][0]  # row
        k11 = k1[1][0]  # column
        k20 = k2[0][0]  # row
        k21 = k2[1][0]  # column
        if(k10 == k20):  # same row
            if(new[x].isupper()):
                plain += key[k10][(k11 - 1) % 5]
            else:
                plain += key[k10][(k11 - 1) % 5].lower()

            if(new[x + 1].isupper()):
                plain += key[k20][(k21 - 1) % 5]
            else:
                plain += key[k20][(k21 - 1) % 5].lower()

        if(k11 == k21):  # same column
            if(new[x].isupper()):
                plain += key[(k10 - 1) % 5][k11]
            else:
                plain += key[(k10 - 1) % 5][k11].lower()
            if(new[x + 1].isupper()):
                plain += key[(k20 - 1) % 5][k21]
            else:
                plain += key[(k20 - 1) % 5][k21].lower()

        elif(k10 != k20 and k11 != k21):
            if(new[x].isupper()):
                plain += key[k10][k21]
            else:
                plain += key[k10][k21].lower()
            if(new[x + 1].isupper()):
                plain += key[k20][k11]
            else:
                plain += key[k20][k11].lower()
        x += 2
    for x in j_index:
    	plain = replace_i(x, plain)
    for x in bogus:
    	plain = remove_bogus(x, plain)
    return plain

plain = input('Enter the plain text for encryption : ')
key = [['L', 'G', 'D', 'B', 'A'],
       ['Q', 'M', 'H', 'E', 'C'],
       ['U', 'R', 'N', 'I', 'F'],
       ['X', 'V', 'S', 'O', 'K'],
       ['Z', 'Y', 'W', 'T', 'P']]
key = np.array(key)
x = 0
new = ''
bogus = []
while((x + 1) < len(plain)):
    if(plain[x].upper() == plain[x + 1].upper() or (plain[x].upper() == 'I' and plain[x + 1].upper() == 'J') or (plain[x].upper() == 'J' and plain[x + 1].upper() == 'I')):
        new += plain[x]
        new += 'X'
        bogus.append(x + 1)
        x = x + 1
    else:
        new += plain[x]
        new += plain[x + 1]
        x = x + 2
if((len(plain) + len(bogus)) % 2 == 1):
    new += plain[len(plain) - 1]
    new += 'X'
    bogus.append(len(plain))

print("After padding the plain text : ", new)

cipher = encrypt(new, key)
print("Cipher Text : ", cipher)

plain = decrypt(cipher, key, bogus)
print("DeCiphered Text : ", plain)