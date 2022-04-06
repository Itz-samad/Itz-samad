from datetime import datetime


def time_():
    present = datetime.now()
    return present.strftime("%Y-%m-%d %H:%M:%S")


def time_1():
    present = datetime.now()
    return present.strftime("%m-%d")


def file_():
    d = open('C:\\Users\\Abdulsamad\\Documents\\Zkyte project\\Project1.txt', 'a')
    return d
