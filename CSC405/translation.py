import numpy as np
# # Matrix multiplication
# def mult(matrix1,matrix2):
#     # Matrix multiplication
#     if len(matrix1[0]) != len(matrix2):
#         # Check matrix dimensions
#         print('Matrices must be m*n and n*p to multiply!')
#     else:
#         # Multiply if correct dimensions
#         new_matrix = np.zeros(len(matrix1),len(matrix2[0]))
#         for i in range(len(matrix1)):
#             for j in range(len(matrix2[0])):
#                 for k in range(len(matrix2)):
#                     new_matrixlist(i][j] += matrix1list(i][k]*matrix2[k][j]
#         return new_matrix



# TranMatrix = np.zeros((3,3))
# TranMatrix[0][0]=1
# TranMatrix[0][2]=Tx
# TranMatrix[1][1]=1
# TranMatrix[1][2]=Ty
# TranMatrix[2][2]=1

# RotMatrix = np.zeros((3,3))
# RotMatrix[0][0]=cos(Theta)
# RotMatrix[0][1]=-1*sin(Theta)
# RotMatrix[1][0]=sin(Theta)            
# RotMatrix[1][1]=cos(Theta)
# RotMatrix[2][2]=1

# translated=mult(TranMatrix, original)

A = []
B = []
C = []

count = 0
while count <= 1:
    A.append(input('Enter the first co-ordinate: '))
    B.append(input('Enter the second co-ordinate: '))
    C.append(input('Enter the third co-ordinate: '))
    count += 1

d_x = input('Entre  the value of dx: ')
d_y = input('Entre the value of dy: ')
A = np.asarray(A)
# for i in A:
    # print(i)
class trans():
    def __init__(self , dx, dy, x, y):
        self.dx = dx
        self.dy = dy
        self.x = x
        self.y = y
        
        
    def by_3(self):
        transmatrix = np.zeros((3,3))
        transmatrix[0][0] = 1
        transmatrix[0][2] = self.dx
        transmatrix[1][1] = 1
        transmatrix[1][2] = self.dy
        transmatrix[2][2] = 1
        # print(transmatrix)
        return transmatrix
    
    def by_1(self):
        tran = np.ones((3, 1))
        tran[0][0] = self.x
        tran[1][0] = self.y
        # print(tran)
        return tran

a = trans(d_x, d_y, A[0], A[1])
# a.by_3()
# a.by_1()
a_1 = np.dot(a.by_3(), a.by_1())
print('\n\t\t{} * {} = {}\n\t\t'.format(a.by_3(), a.by_1(), a_1))

b = trans(d_x, d_y, B[0], B[1])
# b.by_3()
# b.by_1()
b_1 = np.dot(b.by_3(), b.by_1())
print('\n\t\t{} * {} = {}\n\t\t'.format(b.by_3(), b.by_1(), b_1))

c = trans(d_x, d_y, C[0], C[1])
# c.by_3()
# c.by_1()
c_1 = np.dot(c.by_3(), c.by_1())
print(
'\n\t\t{}                  *       {}               =            {}\n\t\t'.format(c.by_3(), c.by_1(), c_1)
)


