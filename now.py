# from req import requ

# import random
# while 1 < 2:
#     m = random.randint(0000, 9999999)
#     print(requ(m))



import csv
with open('emails.csv', 'r') as f:
    fe = csv.reader(f)
    l = []
    for i in fe:
        for e in i:
            # print(i)
            # print(e)
            l.append(e)
            print(l)
            with open('email.csv', 'w') as g:
                g.writelines('{}'.format(l))
                print('succes')   
        

        