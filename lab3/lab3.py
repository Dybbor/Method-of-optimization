import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from sympy import symbols, diff,sin

def func(x, y):
    return (np.sin(x) * np.sin(y)) / (x * y)

def func_min(point):
    x,y = point
    return (np.sin(x) * np.sin(y)) / (x * y)

x = np.arange(-6, 6, 0.1)
y = np.arange(-6, 6, 0.1)

X,Y = np.meshgrid(x, y)
Z = func(X,Y)

start_point = [0.1, 0.5]
min = minimize(func_min, x0=start_point)

color_level = 10
lvl_region = np.linspace(np.min(Z), np.max(Z),color_level).tolist()
color_fill = np.zeros((color_level, 3))
color_fill[:, 1:] = 0.1
color_fill[:, 0] = np.linspace(0, 1, color_level)

fig = plt.figure(figsize=(17,8))
ax = fig.add_subplot(1,2,1, projection = '3d')
ax.plot_surface(X, Y, Z, alpha = 0.8, color='green')
plt.title("График функции ")
ax.scatter(start_point[0], start_point[1], func(start_point[0], start_point[1]), color= "red", s = 100, alpha = 1)
ax.scatter(min.x[0], min.x[1], func_min(min.x), color= "blue", s= 100, alpha =1)


ax = fig.add_subplot(1,2,2)
ax.contourf(X, Y, Z,levels = lvl_region, colors = color_fill)
cs = ax.contour(X, Y, Z,15, colors = "white")
ax.clabel(cs,inline = True, colors = "white", fontsize = 7)
plt.scatter(x = start_point[0],y = start_point[1], color= "blue", s = 200)
plt.scatter(x = min.x[0], y = min.x[1], color= "white", s = 200)
plt.title("Линии уровня")

x1, x2 = symbols("x y")
string_func = ((sin(x1) * sin(x2)) / (x1 * x2))
df_dx = diff(string_func,x1)
df_dy = diff(string_func, x2)
print(f"Gradient : \n\tdf\dx = {df_dx}\n\tdf\dy = {df_dy}")
plt.show()

