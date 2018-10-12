import numpy as np
from polinom import Polinom

def cubic_splain():
    a = []
    b = []
    c = []
    d = []
    h = []
    point = []
    file = open("point.txt" ,'r', encoding="utf-8")
    while True:
        line = file.readline().split(" ")
        if (len(line) <= 1):
            break
        line[0] = float(line[0])
        line[1] = float(line[1])
        point.append([line[0] , line[1]])
    n = len(point) - 1
    a = np.zeros(n)
    b = np.zeros(n)
    c = np.zeros(n + 1)
    d = np.zeros(n)
    h = np.zeros(n)

    for i in range(n):
        a[i] =  point[i][1]

    for i in range(n):
        h[i] = point[i + 1][0] - point[i][0]

    Matrix = np.zeros((n - 1, n - 1))

    Matrix[0][0] = 2 * (h[0] + h[1])
    Matrix[0][1] = h[1]

    for i in range(1, n - 2):
        Matrix[i][i - 1] = h[i]
        Matrix[i][i] = 2 * (h[i] + h[i+1])
        Matrix[i][i + 1] = h[i + 1]

    Matrix[n - 2][n - 3] = h[n - 2]
    Matrix[n - 2][n - 2] = 2 * (h[n - 2] + h[n - 1])

    F = np.zeros(n-1)
    for i in range(1, n):
        F[i - 1] = 3 * ((point[i + 1][1] - point[i][1]) / h[i] - (point[i][1] - point[i-1][1]) / h[i - 1])

    tmp = np.linalg.solve(Matrix, F)

    for i in range(1, n):
        c[i] = tmp[i - 1]
    
    for i in range(n): 
        d[i] = (c[i + 1] - c[i]) / (3 * h[i])


    for i in range(n):
        b[i] = ((point[i + 1][1] - point[i][1]) / h[i]) - (h[i] / 3) *(c[i + 1] + 2 * c[i])

    c.pop([2])
    print(point)
    print(a)
    print(b)
    print(c)
    print(d)
    



cubic_splain()
