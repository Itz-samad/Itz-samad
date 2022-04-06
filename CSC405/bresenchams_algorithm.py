import matplotlib.pyplot as plt


def bren_all(x0, y0, x1, y1):
    x_ax = []
    y_ax = []
    dx = x1 - x0
    dy = y1 - y0
    dy_2 = 2 * dy 
    p_k = (2 * dy) - dx
    init_x = x0
    init_y = y0
    x_k = x0
    y_k = y0
    print('PK | P_K1 | X_K1 | Y_K1')
    print('________________________')
    print('    |      |  {}  |  {}'.format(x_k, y_k,))
    print('________________________')
    while x_k != x1 or y_k != y1:
        if p_k < 0:
            P_K1 = p_k + dy_2
            x_k = init_x + 1
            y_k = y_k
            x_ax.append(x_k)
            y_ax.append(y_k)
            
        elif p_k > 0:
            P_K1 = p_k + ((2 * dy) - (2 * dx))
            x_k = init_x + 1
            y_k = init_y + 1
            x_ax.append(x_k)
            y_ax.append(y_k)
           
        init_x = x_k
        init_y = y_k
        
        print('{}  |  {}  |  {}  |  {}'.format(p_k,P_K1,x_k, y_k,))
        print('________________________')
        p_k = P_K1
    
    plt.plot(x_ax, y_ax)
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.title("Graph of x and y")
    plt.show()
    
        
