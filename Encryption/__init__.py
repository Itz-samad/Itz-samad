from decrypt import decrypt
from encrypt import encrypt
from key import key
import csv
import json
import numpy as np


def main():
    
    quotes = []
    quote = {}
 
    # quote['File Encrypted'] = pass
    # quote['Pass Key'] = pass
    # quote['File Decrypted'] = pass
    
   

    print('\n\n\t\tWelcome To the encryptor \n\n'
    '\t\n\t\t What would you like to do\n'
    )
    d = decrypt
    e = encrypt
    k = key
    counters = 0
    while counters <= 2:
        try:
            g = int(input(
                '\n\t\t Enter: \n\n'
                '\n\t\t 1. To Generate a Pass key,\n'
                '\n\t\t 2. to Encrypt A File,\n'
                '\n\t\t 3. To Decrypt A File,\n'
                '\n\t\t 4. To End the program,\n'
                '\n\n\t\t>>>\t'
            ))
        except ValueError:
            g =  None 
        if g is not None:
            if g == 1:
                try:
                    u = input('\n \tPlease Enter ther file name you wish to save your pass key to: ')
                    k(filename=u)
                except FileNotFoundError:
                    print('\n\tNO SUCH FILE OR DIRECTORY\n')
            elif g == 2:
                try:
                    u = input('\n\tPlease Enter the file to be Encrypted: ')
                    n = input('\n\tPlease Enter the name of the pass key file: ')
                    # e(file_path=u, pass_key_name=n)
                    t = e(file_path=u, pass_key_name=n)
                    quote['File Encrypted'] = u
                    quote['Pass File'] = '{}.key'.format(n)
                    quote['Pass Key'] = t
                    quotes.append(quote)
                except PermissionError:
                    print('\n\tPERMISION DENIED\n')
                except FileNotFoundError:
                    print('\n\tNO SUCH FILE OR DIRECTORY\n ')
            elif g == 3:
                try:
                    u = input('\n\tPlease Enter the file name to be Decrypted: ')
                    n = input('\n\tPlease Enter the name of the pass key file: ')
                    t = d(filename=u, file_path=n)
                    quote['File Decrypted'] = u 
                    quote['Pass File'] = '{}.key'.format(n)
                    quote['Pass Key'] = t
                    quotes.append(quote)
                    print(quotes)
                # except InvalidToken:
                #     print('INVALID TOKEN')
                except PermissionError:
                    print('\n\tPERMISION DENIED\n')
                except FileNotFoundError:
                    print('\n\tNO SUCH FILE OR DIRECTORY \n')
            elif g == 4:
                counters = 3
                print('\n\n\t\tQuiting The Programme.................\n\n')
            else:
                print('Wrong input')
        else:
            print('Wrong input format, try integer value')
        
        # for i in quotes:
            # print(i)

        # r = {'File Encrypted': 'None'}
        # b = {'File Decrypted': 'None'}


        # for i in quotes:
            # new_dict = i.pop(b)
            # print(new_dict)

        
        # for i in quotes:
            # new_dict2 = i.pop(r)
            # print(new_dict2)
        # for l in quotes:
        #     for each in l:
        #         print(each)
        #         if r in l:
        #             u = None
        #         elif b in l:
        #             k = None
        class MyEncoder(json.JSONEncoder):
            def default(self, obj):
                if isinstance(obj, np.ndarray):
                    return obj.tolist()
                elif isinstance(obj, bytes):
                    return str(obj, encoding='utf-8')
                return json.JSONEncoder.default(self, obj)


        # with open('process.json', 'r', encoding='utf-8') as p:
            # data = json.load(p)
        # with open("process.json", "w", encoding='utf-8') as f:
        #     for o in quotes:
        #         if u is not None:
        #             print(type(o))
        #             o[b] = 'None'
        #             json.dump(o, f, indent = 10)
                    
        #         elif k is not None:
        #             print(o)
        #             o[r] = 'None'
        #             json.dump(o, f, indent = 10)
                    
            
        #         else:
        #             print('ahoy')


main()