from cryptography.fernet import Fernet 
def decrypt(filename, file_path):
    with open('{}.key'.format(file_path), 'rb') as filekey:
        key = filekey.read()
        print('Succesfully read the Pass key')

    fernet = Fernet(key)

    with open('{}'.format(filename), 'rb') as enc_file:
        encrypted = enc_file.read()
        print('Succesfully read th encrypted file')

    decrypted = fernet.decrypt(encrypted)
    with open('{}'.format(filename), 'wb') as dec_file:
        dec_file.write(decrypted)
    print('Succesfully Decrypted the File')
    return key
