import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy.optimize import minimize
from sympy import symbols, diff, nsolve


def funcQ(x, y):
    return 4*x**2 + 2*x*y+y**2+2

# border x y
xLeftBorder = -5
xRightBorder = 5
yLeftBorder = -5
yRightBorder = 5

x = np.arange(xLeftBorder, xRightBorder, 0.01)
y = np.arange(yLeftBorder, yRightBorder, 0.01)

X,Y = np.meshgrid(x, y)
Z = funcQ(X,Y)


ax = plt.axes(projection = "3d")
ax.plot_surface(X, Y, Z, cmap = cm.gist_earth)


level = 17
fig, ax = plt.subplots()
plt.title("Линии уровня")
plt.xlim(xLeftBorder, xRightBorder)
plt.ylim(yLeftBorder,yRightBorder)

specialXforSqrt = np.arange(-4, 2, 0.01)

ax.contourf(X, Y, Z,levels = level, cmap = cm.gist_earth)
ax.fill_between(x, yLeftBorder, yRightBorder,where = ((x >  2)) , color = 'lightgreen',hatch='X', alpha  = 0.5)
ax.fill_between(x, yLeftBorder, yRightBorder,where = ((x < -4)) , color = 'lightgreen',hatch='X', alpha  = 0.5)
ax.fill_between(specialXforSqrt,-np.sqrt(9-(specialXforSqrt+1)**2)-1, yLeftBorder, color = 'lightgreen',hatch='X', alpha = 0.5)
ax.fill_between(specialXforSqrt, np.sqrt(9-(specialXforSqrt+1)**2)-1, yRightBorder, color = 'lightgreen',hatch='X', alpha = 0.5, label = r'g1 = $(x+1)^2+(y+1)^2-9$')
ax.fill_between(x, -0.5*x -0.5, yRightBorder, color = "lightcoral", hatch = "//", alpha = 0.5, label = "g2 = 0.5x + y + 0.5")
ax.fill_between(x, 2*x -1 , yRightBorder, color = 'lightblue', hatch="\\", alpha = 0.7, label = "g3 = -2x + y + 1")
cs = ax.contour(X, Y, Z,levels = level, colors = "black", alpha =0.7)
ax.clabel(cs,inline = True, colors = "black", fontsize = 9)
plt.legend(bbox_to_anchor=(1, 1), loc="best", borderaxespad=0.)


x, y = symbols("x y")
mu1, mu2, mu3 = symbols("mu1 mu2 mu3")
funcQ = 4*x**2 + 2*x*y+y**2+2
g1 = (x+1)**2+(y+1)**2-9
g2 = 0.5*x + y + 0.5
g3 = -2*x + y + 1

lagrange = funcQ
dl_dx = diff(funcQ, x)
dl_dy = diff(funcQ, y)
res = nsolve((dl_dx, dl_dy), (x,y), (0,0))
ax.scatter(res[0], res[1], color = 'white')
print('1', res)

lagrange = funcQ + mu2*g2+ mu3*g3
dl_dx = diff(lagrange, x)
dl_dy = diff(lagrange, y)
dl_mu2 = diff(lagrange, mu2)
dl_mu3 = diff(lagrange, mu3)
print(dl_dx, dl_dy, dl_mu2, dl_mu3, sep='\n')
res = nsolve((dl_dx, dl_dy, dl_mu2, dl_mu3), (x,y, mu2, mu3), (0,0,0,0))
print('2' ,res)
ax.scatter(res[0], res[1], color = 'red')
plt.show()

