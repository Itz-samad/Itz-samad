from utils import time_, file_
from new4 import write_2
from new3 import okpe
f = file_()
diction = {}
current_time = time_()
# this is to input tell if the buyer wants to either write to the file or retrieve from the file
print('Welcome to the E-Journal Created by yours truly @Black_Diamond')
gone = eval(input("Enter 1 to write your task of the day or Enter 2 to retrieve a saved file: "))
number = 1
if gone == 1:
    write_2()


elif gone == 2:
    okpe()


else:
    print('wrong input') 

f.close()
