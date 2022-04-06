from cryptography.fernet import Fernet

def encrypt(file_path, pass_key_name):
	with open('{}.key'.format(pass_key_name), 'rb') as filekey:
		key = filekey.read()
		print('Succeeded Read the Pass Key')

	fernet = Fernet(key)

	with open('{}'.format(file_path), 'rb') as file:
		original = file.read()
		print('Succesfully Read the File to be Encrypted')
	
		# encrypting the file
	encrypted = fernet.encrypt(original)

	with open('{}'.format(file_path), 'wb') as encrypted_file:
		encrypted_file.write(encrypted)
		
	print('Succesfully Encrypted The File')
	return key


