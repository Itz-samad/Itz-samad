from cryptography.fernet import Fernet

def key(filename):
	key = Fernet.generate_key()
	with open('{}.key'.format(filename), 'wb') as f:
		f.write(key)
	print('Pass Key Succesfully Generated')