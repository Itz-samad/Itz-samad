def now_2():
    time = []
    month = input('Enter the month: ')
    day = input('Enter the day: ')    
    time.append(month)
    time.append(day)
    return time


def okpe():
    global goods
    visa = now_2()
    ori = (visa[0] + '-' + visa[1])
    ba = open("C:\\Users\\Abdulsamad\\Documents\\Zkyte project\\Project1.txt", 'r')
    info = ba.read()
    con = 1
    bo = int(visa[1])
    bod = bo + con
    bods = str(bod)
    boda = str('0' + bods)
    bigi = ('-' + boda)
    if ori in info:
        g = info.find(bigi)
        f = info.find(ori)
        goods = info[f:g]
        print(goods)
        lina = goods.find(info)
        goods = goods[lina:]

    else:
        print("\n \n \t \tNOT IN FILE\n \n")





