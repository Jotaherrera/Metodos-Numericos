import numpy as np

# 1 2x2

A = [[3, -4], [2, 4]]
B = [[-6], [16]]

INV_A = np.linalg.inv(A)
Solution = np.dot(INV_A, B)
print(f"1) x,y: \n{Solution}")

# 2 3x3
A2 = [[3, 2, 1], [5, 3, 4], [1, 1, -1]]
B2 = [[1], [2], [1]]

INV_A2 = np.linalg.inv(A2)
Solution = np.dot(INV_A2, B2)
print(f"2) x,y,z: \n{Solution}")

# 3 4x4
A3 = [[1, -2, 2, -3], [3, 4, -1, 1], [2, -3, 2, -1], [1, 1, -3, -2]]
B3 = [[15], [-6], [17], [-7]]

INV_A3 = np.linalg.inv(A3)
Solution = np.dot(INV_A3, B3)
print(f"3) w, x,y,z: \n{Solution}")

# 4 5x5
A4 = [
    [2, -1, 4, 1, -1],
    [-1, 3, -2, -1, 2],
    [5, 1, 3, -4, 1],
    [3, -2, -2, -2, 3],
    [-4, -1, -5, 3, -4],
]
B4 = [[7], [1], [33], [24], [-49]]

INV_A4 = np.linalg.inv(A4)
Solution = np.dot(INV_A4, B4)
print(f"4) x,y,z,t,u: \n{Solution}")

# 5 6x6
A5 = [
    [1, 1, 1, 0, 1, 0],
    [-1, -2, 1, 1, 2, 1],
    [1, 4, 0, 1, 0, 2],
    [8, 1, 8, 0, 1, 0],
    [-8, -2, 8, 8, 2, 1],
    [8, 3, 0, 8, 0, 2],
]
B5 = [[1], [0], [0], [0], [0], [0]]

INV_A5 = np.linalg.inv(A5)
Solution = np.dot(INV_A5, B5)
print(f"5) a,b,c,d,e,f: \n{Solution}")
