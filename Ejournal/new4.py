from utils import time_, file_, time_1
f = file_()
diction = {}
current_time = time_()


def write_2():
    number = 1
    counter = 10
    from new2 import add_values_in_dict
    add_values_in_dict(diction, current_time)
    f.writelines("\n \t \t Welcome to the E- journal Created by  yours truly @Black_Diamond")
    f.writelines("\n  \t  \t \t  Today's time and date: {}\n".format(current_time))
    f.writelines('\n {}:'.format(time_1()))
    for val in diction[current_time]:
        f.writelines('\n \n \n  {}. {}'.format(number, val))
        counter += 1
        number += 1
    f.writelines('\n')
    f.writelines('-' * 150)
    return print(diction)









