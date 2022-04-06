import matplotlib.pyplot as plt


def mid_all(x0, y0, x1, y1):
    x_ax = []
    y_ax = []
    init_x = x0 
    init_y = y0
    dx = x1 - x0
    dy = y1 - y0
    d_o = (2 * dy) - dx
    print(d_o)
    dy_e = 2 * dy
    dy_ne = 2 * (dy - dx)
    x_k = x0
    y_k = y0
    print('d | X_K1 | Y_K1')
    print('________________________')
    print('     |  {}  |  {}'.format(x_k, y_k,))
    print('________________________')
    while x_k != x1 or y_k != y1: 
        if d_o <= 0:
            print('you go East')
            d_new = d_o + dy_e
            x_k = init_x + 1
            y_k = y_k
            x_ax.append(x_k)
            y_ax.append(y_k)

        elif d_o >= 0:
            print('you go North East')
            d_new = d_o + dy_ne
            x_k = init_x + 1
            y_k = init_y + 1
            x_ax.append(x_k)
            y_ax.append(y_k)

        init_x = x_k
        init_y = y_k
        print(' {}  |  {}  |  {}'.format(d_o,x_k, y_k,))
        print('________________________')   
        d_o = d_new 
            

        

    
    plt.plot(x_ax, y_ax)
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.title("Graph of x and y")
    plt.show()
    
        
