# Affine cipher
def encrypt(plain, key1, key2):
	cipher = ''
	for x in plain:
		if(x.isupper()):
			cipher += chr(((((ord(x) - 65) * key1) + key2) % 26) + 65)
		elif(x.islower()):
			cipher += chr(((((ord(x) - 97) * key1) + key2) % 26) + 97)
	return cipher

def decrypt(cipher, inv_key, key2):
	plain = ''
	for x in cipher:
		if(x.isupper()):
			plain += chr((((ord(x) - 65 - key2) * inv_key) % 26) + 65)
		elif(x.islower()):
			plain += chr((((ord(x) - 97 - key2) * inv_key) % 26) + 97)
	return plain

def multiplicative_inverse(b, n):
	ra = n
	rb = b
	ta = 0
	tb = 1
	while(rb > 0):
		q = ra // rb
		r = ra - q * rb
		ra = rb
		rb = r
		t = ta - q * tb
		ta = tb
		tb = t
	if(ra == 1):
		if(ta > 0):
			return ta
		else:
			return (ta % 26)
	else:
		return(-1)

plain = input('Enter the plain text for encryption : ')
key1, key2 = map(int, input('Enter the value of keys (k1 and k2): ').split())
cipher = encrypt(plain, key1, key2)
print('Cipher Text : ', cipher)
inv_key = multiplicative_inverse(key1, 26)
if(inv_key == -1):
	print('Multiplicative Inverse of the given key not possible !')
else:
	plain = decrypt(cipher, inv_key, key2)
	print('DeCiphered Text : ', plain)