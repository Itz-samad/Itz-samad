from dda_algorithm import dda_all
from bresenchams_algorithm import bren_all
from midpoints_algorithm import mid_all
o = int(input('\n\tEnter the Value of x0: '))
a = int(input('\n\tEnter the Value of y0: '))
f = int(input('\n\tEnter the Value of x1: '))
r = int(input('\n\tEnter the Value of y1: '))

def first(x0, y0, x1, y1):
    counter = 0
    while counter < 1:
        t = input('\n\tWhich Algorithm will u like to use to solve the co-ordinate: '
                '\n\t 1. DDA ALGORITHM\n'
                '\n\t 2. BRESENCHAMS ALGORITHM\n'
                '\n\t 3. MIDPOINTS ALGORITHM\n'
                '\n\t 4. Change the co-ordinates\n' 
                '\n\t 5. End the program\n'
                '\n\t >> '     
        )
        if t == '1':
            dda_all(x0, y0, x1, y1)
        elif t == '2':
            bren_all(x0, y0, x1, y1)
        elif t == '3':
            mid_all(x0, y0, x1, y1)
        elif t == '4':
            x0 = int(input('\n\tEnter the Value of x0: '))
            y0 = int(input('\n\tEnter the Value of y0: '))
            x1 = int(input('\n\tEnter the Value of x1: '))
            y1 = int(input('\n\tEnter the Value of y1: '))
            print('\n\tchanging co-ordinates......................\n\t')
            print('\n\tco-ordinate Successfuly changed\n\t')
        elif t == '5':
            y = input('\n\tAre you sure u want to quit.......... ')
            if y.lower() == 'yes':
                print('Quiting programme.............. \n\t')
                counter = 2
            elif y.lower() == 'no':
                counter = 0
            else:
                print('\n\twrong input\n\t')
        
        else:
            print('\n\tWrong input\n\t')

first(o, a, f, r)
