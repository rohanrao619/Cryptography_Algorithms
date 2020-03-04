def encrypt(plain, key):
	cipher = ''
	for x in plain:
		if(x.isupper()):
			cipher += chr(((ord(x) - 65 + key) % 26) + 65)
		elif(x.islower()):
			cipher += chr(((ord(x) - 97 + key) % 26) + 97)
	return cipher

def decrypt(cipher, key):
	plain = ''
	for x in cipher:
		if(x.isupper()):
			plain += chr(((ord(x) - 65 - key) % 26) + 65)
		elif(x.islower()):
			plain += chr(((ord(x) - 97 - key) % 26) + 97)
	return plain

plain = input('Enter the plain text for encryption : ')
key = int(input('Enter the value of key : '))
cipher = encrypt(plain, key)
print('Cipher Text : ', cipher)
plain = decrypt(cipher, key)
print('DeCiphered Text : ', plain)