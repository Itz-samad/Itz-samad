import matplotlib.pyplot as plt


def dda_all(x0, y0, x1, y1):
    """
    Getting the two point (x0,y0) and (x1,y1) 
    compairing by finding the difference to get steps  i.e 
    absolute change in dx or dy. Which will be the highest difference.
    
    """
    x_ax = []
    y_ax = []
    my_dict = {}

    dx = x1 - x0
    dy = y1 - y0
    """
    Once the highest is found, both the difference  dx and dy will be divided by that with the highest difference.
    This line of code is for when dx is the highest.
    """
    if dx >= dy:
        steps = abs(dx)
        # print(steps)
        x_inc = dx / steps
        y_inc = dy / steps
        init_x = x0
        init_y = y0
        """
        Itration starts here
        Then itration will begin by adding the current value of x and y to thier previous 
        value to get a new value for each.
        This  continue till itration has been done for the steps value.
        """
        for i in range(steps):
            x_ = init_x + x_inc
            init_x = x_
            y_ = init_y + y_inc
            init_y = y_
            my_dict['x'] = round(init_x)
            my_dict['y'] = round(init_y)
            x_ax.append(my_dict['x'])
            y_ax.append(my_dict['y'])
            print("\n\t('x' : {}, 'y' : {},          |          'x' : {}, 'y' : {})\n".format(float(init_x), float(init_y), my_dict['x'], my_dict['y']))
    # This line of code is for when dy is the highest.
    elif dy >= dx:
        steps = abs(dy)
        print(steps)
        x_inc = dx / steps
        y_inc = dy / steps
        init_x = x0
        init_y = y0  
        #Itration starts here.
        for i in range(steps):
            x_ = init_x + x_inc
            init_x = x_
            y_ = init_y + y_inc
            init_y = y_
            my_dict['x'] = round(init_x)
            my_dict['y'] = round(init_y)
            x_ax.append(my_dict['x'])
            y_ax.append(my_dict['y'])
            print("\n\t('x' : {}, 'y' : {},          |          'x' : {}, 'y' : {})\n".format(float(init_x), float(init_y), my_dict['x'], my_dict['y']))
            
            

    plt.plot(x_ax, y_ax)
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.title("Graph of x and y")
    plt.show()

