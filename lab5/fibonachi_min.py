# def fibonacci(x): 
#     if x <= 2 :
#         return 1
#     return fibonacci(x-1)+ fibonacci(x-2)

# def func(x):
#     return (x**3) /3  - (x**2) /2 - x -1


# al = []
# bl = []
# xl = []
# yl = []

# a = 1 
# b = 2
# n = 12
# eps = 0.00000000000000001
# sigma = 0.01

# count = 0
# while((b-a)/fibonacci(count)>sigma):
#     count +=1
#     print("count ",count)

# k = 0
# for i in range (0, n-2):
#     x = b - (b-a)*fibonacci(n - k - 1 )/ fibonacci(n - k)
#     y = a + (b-a)*fibonacci(n - k - 1 )/ fibonacci(n - k)
#     print(i)
#     k+=1
#     print(f"{a,b}")
#     print(f" x = {x} ,  y = {y}")
#     qx, qy = func(x), func(y)
#     print(f"fx = {qx} , fy = {qy}\n")

#     al.append(a)
#     bl.append(b)
#     xl.append(x)
#     yl.append(y)
#     if (qx < qy):
#         b = y
#         y = x
#     else:
#         a = x
#         x = y


import numpy as np

a = map({"points": np.array([[1,2], [2,1]])})
print(a)

point = {"points", (1,1,0)}
    
    
