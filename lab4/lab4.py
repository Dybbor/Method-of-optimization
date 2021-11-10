import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy.optimize import minimize
from sympy import symbols,diff, nsolve, cos, sin



def funcQ(x, y):
    return 20*(np.cos(3*x) - y)**2 + (y -4*x)**2
    
# border x y
xLeftBorder = -1.5
xRightBorder = 2
yLeftBorder = -2 
yRightBorder = 2

x = np.arange(xLeftBorder, xRightBorder, 0.01)
y = np.arange(yLeftBorder, yRightBorder, 0.01)

X,Y = np.meshgrid(x, y)
Z = funcQ(X,Y)


ax = plt.axes(projection = "3d")
ax.plot_surface(X, Y, Z, cmap = cm.gist_earth)


level = 17
fig, ax = plt.subplots()
plt.title("Линии уровня")
g1 = X + Y - 0.1
plt.xlim(-1.5,2)
plt.ylim(-2,2)

specialXforSqrt = np.arange(-1.23, 2, 0.01)

ax.contourf(X, Y, Z,levels = level, cmap = cm.gist_earth)
ax.fill_between(x, -x + 0.1 , yRightBorder, color = 'lightblue',hatch="\\", alpha = 0.8, label = "g1 = y + x-0.1")
ax.fill_between(x, x + 0.25, 2, color = "lightcoral", hatch = "//", alpha = 0.6, label = "g3 = y - x -0.25")
ax.fill_between(specialXforSqrt,-np.sqrt((-(specialXforSqrt-1)**2+5)/2)+1, 1, color = 'lightgreen',hatch='X', alpha = 0.6)
ax.fill_between(specialXforSqrt, np.sqrt((-(specialXforSqrt-1)**2+5)/2)+1, 1, color = 'lightgreen',hatch="X", alpha = 0.6, label = r"$g2 = -(x-1)^2-2(y-1)^2+5$")
cs = ax.contour(X, Y, Z,levels = level, colors = "black", alpha =0.7)
ax.clabel(cs,inline = True, colors = "black", fontsize = 9)
plt.legend(bbox_to_anchor=(1, 1), loc="best", borderaxespad=0.)


x, y = symbols("x y")
mu1, mu2, mu3 = symbols("mu1 mu2 mu3")
funcQ = 20*(cos(3*x) - y)**2 + (y -4*x)**2
g1 = y + x  - 0.1
g2 = -(x-1)**2-2*(y-1)**2+5 
g3 = y - x -0.25


# # без учета ограничений
# dq_dx = diff(funcQ, x)
# dq_dy = diff(funcQ, y)
# fx, fy = nsolve((dq_dx, dq_dy),(x,y), (0,0))
# print(f"без ограничений:") 
# print(f'dq_dx: {dq_dx}')
# print(f'dq_dy: {dq_dy}')
# print(f'answer {fx, fy}')
# ax.scatter(fx, fy, color= "blue", s= 100, alpha =1)
# plt.show()

# # c учетом трех ограничений
# lagrange = funcQ + mu1*g1 + mu2*g2 + mu3*g3
# l_dx = diff(lagrange,x)
# l_dy = diff(lagrange, y)
# l_mu1 = diff(lagrange, mu1)
# l_mu2 = diff(lagrange, mu2)
# l_mu3 = diff(lagrange, mu3)
# print(l_dx, l_dy, l_mu1, l_mu2, l_mu3, sep='\n')
# answer =  nsolve((l_dx, l_dy, l_mu1, l_mu2, l_mu3), (x, y, mu1, mu2, mu3), (0,0,0,0,0))
# print(answer)

# # c учетом 2 и 3 ограничений
# lagrange = funcQ + mu2*g2 + mu3*g3
# l_dx = diff(lagrange,x)
# l_dy = diff(lagrange, y)
# l_mu2 = diff(lagrange, mu2)
# l_mu3 = diff(lagrange, mu3)
# print(l_dx, l_dy, l_mu2, l_mu3, sep='\n')
# answer =  nsolve((l_dx, l_dy, l_mu2, l_mu3), (x, y, mu2, mu3), (0,0,0,0))
# print(answer)
# print(f'g2 check {g2.subs(x, answer[0]).subs(y,answer[1])}')
# print(f'g3 check {g3.subs(x, answer[0]).subs(y,answer[1])}')
# ax.scatter(answer[0], answer[1], color= "blue", s= 100, alpha =1)
# plt.show()

# # c учетом 1 и 2 ограничений
# lagrange = funcQ + mu1*g1 + mu2*g2
# l_dx = diff(lagrange,x)
# l_dy = diff(lagrange, y)
# l_mu1 = diff(lagrange, mu1)
# l_mu2 = diff(lagrange, mu2)
# print(l_dx, l_dy, l_mu1, l_mu2, sep='\n')
# answer =  nsolve((l_dx, l_dy, l_mu1, l_mu2), (x, y, mu1, mu2), (0,0,0,0))
# print(answer)
# print(f'g1 check {g1.subs(x, answer[0]).subs(y,answer[1])}')
# print(f'g2 check {g2.subs(x, answer[0]).subs(y,answer[1])}')
# print(f'g3 check {g3.subs(x, answer[0]).subs(y,answer[1])}')
# ax.scatter(answer[0], answer[1], color= "blue", s= 100, alpha =1)
# plt.show()

# # c учетом 1 и 3 ограничений
# lagrange = funcQ + mu1*g1 + mu3*g3
# l_dx = diff(lagrange,x)
# l_dy = diff(lagrange, y)
# l_mu1 = diff(lagrange, mu1)
# l_mu3 = diff(lagrange, mu3)
# print(l_dx, l_dy, l_mu1, l_mu3, sep='\n')
# answer =  nsolve((l_dx, l_dy, l_mu1, l_mu3), (x, y, mu1, mu3), (0,0,0,0))
# print(answer)
# print(f'g1 check {g1.subs(x, answer[0]).subs(y,answer[1])}')
# print(f'g2 check {g2.subs(x, answer[0]).subs(y,answer[1])}')
# print(f'g3 check {g3.subs(x, answer[0]).subs(y,answer[1])}')
# ax.scatter(answer[0], answer[1], color= "blue", s= 100, alpha =1)
# plt.show()


# # c учетом 1 
# lagrange = funcQ + mu3*g3
# l_dx = diff(lagrange,x)
# l_dy = diff(lagrange, y)
# l_mu3 = diff(lagrange, mu3)
# print(l_dx, l_dy, l_mu3,sep='\n')
# answer = nsolve((l_dx, l_dy, l_mu3), (x, y, mu3), (0,0,0))
# print(answer)
# print(f'g1 check {g3.subs(x, answer[0]).subs(y,answer[1])}')
# ax.scatter(answer[0], answer[1], color= "blue", s= 1, alpha =1)
# plt.show()

# print('asdf  ',l_dy.subs(x,-0.127255605943562).subs(y,0.122744394056438))


# c учетом 2
lagrange = funcQ + mu2*g2
l_dx = diff(lagrange,x)
l_dy = diff(lagrange, y)
l_mu2 = diff(lagrange, mu2)
print(l_dx, l_dy, l_mu2,sep='\n')
answer = nsolve((l_dx, l_dy, l_mu2), (x, y, mu2), (0,0,0))
print(answer)
print(f'g1 check {g3.subs(x, answer[0]).subs(y,answer[1])}')
ax.scatter(answer[0], answer[1], color= "red", s= 100, alpha =1)
plt.show()

# #g3
# answers = []
# start = -0.17
# while (start < 2):
#     new_x = start 
#     new_y =  start + 0.25
#     isIt = 32*x - 8*y - 120*(-y + cos(3*x))*sin(3*x)
#     temp = isIt.subs(x, new_x).subs(y,new_y)
#     print(start, temp, sep = '  ||  ')
#     if (temp >= 0):
#         answers.append([new_x,new_y, temp])
#         ax.scatter(new_x, new_y, color= "red", s= 100, alpha =1)   
#     start += 0.001



# answers= []
# start = -1 
# while(start < 2): 
#     new_x = start
#     new_y = -np.sqrt((-(new_x-1)**2+5)/2)+1
#     start += 0.1
#     lagrange = funcQ + mu2*g2
#     l_dy = diff(lagrange, y)
#     temp = l_dy.subs(x, new_x).subs(y, new_y)
#     res = nsolve(temp,0)
#     if (res >=0 ):
#         answers.append([new_x,new_y, temp])
#         ax.scatter(new_x, new_y, color= "blue", s= 100, alpha =1)   
# plt.show()

# temp = l_dy.subs(x,0.0476743278506242).subs(y, -0.430572580151954)
# print(temp)
# res = nsolve(temp,0)
# print(res)

# ax.scatter(-0.127255605943562, 0.122744394056438, color= "red", s= 100, alpha =1)
