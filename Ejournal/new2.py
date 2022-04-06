from utils import time_
current_time = time_()
buy = []
buyer = ''


def inpudict(numkeys=10):
    global buy, buyer
    for dan in range(numkeys):
        if buyer.upper() != 'END':
            print("welcome to E-JOURNAL,\n enter your task of the day below and enter 'END' to quit the programme")
            buyer = input("the time now is {}.\n > ".format(current_time))
            if buyer.upper() != 'END':
                buy.append(buyer)
            else:
                break
        else:
            break
    # diction[buy] = current_time
    return buy


def add_values_in_dict(sample_dict, key, list_of_values=inpudict()):
    if key not in sample_dict:
        sample_dict[key] = list()
    sample_dict[key].extend(list_of_values)
    return sample_dict


file = open('C:\\Users\\Abdulsamad\\Documents\\Zkyte project\\Project1.txt', 'rt')
file = file

# def buba():
#     bridge = 1
#     counter = 1
#     while counter <= 10:
#         ba.append(file.readlines(counter))
#         counter += 1
#         bridge += 1
#     return ba

dican = []


file.close()
