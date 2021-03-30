"""
Workshop 6 Modules
Run this python file using an IDE (vscode, pycharm...)
Be sure to import the modules listed down below!

Some documentation:
https://docs.python.org/3/library/index.html
https://docs.python.org/3/library/random.html
https://docs.python.org/3/library/math.html
"""
# Math example
import math

def quad_formula (a,b,c):
    """Return the solutions to the equation ax^2 +bx +c= 0"""
    disc = b**2 -4*a*c
    root1 = (-b + math.sqrt(disc)) / (2*a)
    root2 = (-b - math.sqrt(disc)) / (2*a)
    return (root1, root2)
roots = quad_formula(1,0,-4)
print(roots)
#----------------------------------------------------------------------------------
import numpy as np
a = np.array([[1, 7],
              [2, 4]])

b = np.array([[3, 3],
              [5, 2]])

c = np.matmul(a, b)
print(c)
#https://www.google.com/search?q=matrix+multiplication&sxsrf=ALeKk00yNXTo_QsjvLOBfauiuDf4OG3J4w:1617077560972&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjJ6OGsk9fvAhVUHTQIHfsXAycQ_AUoAXoECAEQAw&biw=1920&bih=977#imgrc=aDQdgNYdmhg4sM
#https://www.symbolab.com/solver/matrix-calculator/%5Cbegin%7Bpmatrix%7D1%267%5C%5C%20%202%264%5Cend%7Bpmatrix%7D%5Ccdot%5Cbegin%7Bpmatrix%7D3%263%5C%5C%20%205%262%5Cend%7Bpmatrix%7D
#==================================================================================
# matplotlib example
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,4*np.pi,0.1)   # start,stop,step
y = np.sin(x)
z = np.cos(x)

plt.plot(x,y,x,z)
plt.xlabel('x values from 0 to 4pi')  # string must be enclosed with quotes '  '
plt.ylabel('sin(x) and cos(x)')
plt.title('Plot of sin and cos from 0 to 4pi')
plt.legend(['sin(x)', 'cos(x)'])      # legend entries as seperate strings in a list
plt.show()
#----------------------------------------------------------------------------------
# 3D matplotlib example
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes(projection='3d')

def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,cmap='viridis', edgecolor='none')
ax.set_title('surface')
#https://colab.research.google.com/github/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/04.12-Three-Dimensional-Plotting.ipynb
#==================================================================================
# Pygame example
import pygame
import math
import colorsys

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
hue = 0

WIDTH = 1920
HEIGHT = 1080

x_start, y_start = 0, 0

x_separator = 10
y_separator = 20

rows = HEIGHT // y_separator
columns = WIDTH // x_separator
screen_size = rows * columns

x_offset = columns / 2
y_offset = rows / 2

A, B = 0, 0  # rotating animation

theta_spacing = 10
phi_spacing = 10 # for faster rotation change to 2, 3 or more, but first change 86, 87 lines as commented

chars = ".,-~:;=!*#$@"  # luminance index

screen = pygame.display.set_mode((WIDTH, HEIGHT))

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
# display_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Donut')
font = pygame.font.SysFont('Arial', 18, bold=True)

def hsv2rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))


def text_display(letter, x_start, y_start):
    text = font.render(str(letter), True, hsv2rgb(hue, 1, 1))
    display_surface.blit(text, (x_start, y_start))

# def text_display(letter, x_start, y_start):
#     text = font.render(str(letter), True, white)
#     display_surface.blit(text, (x_start, y_start))


run = True
while run:

    screen.fill((black))

    z = [0] * screen_size  # Donut. Fills donut space
    b = [' '] * screen_size  # Background. Fills empty space

    for j in range(0, 628, theta_spacing):  # from 0 to 2pi
        for i in range(0, 628, phi_spacing):  # from 0 to 2pi
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int(x_offset + 40 * D * (l * h * m - t * n))  # 3D x coordinate after rotation
            y = int(y_offset + 20 * D * (l * h * n + t * m))  # 3D y coordinate after rotation
            o = int(x + columns * y)  # 3D z coordinate after rotation
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))  # luminance index
            if rows > y and y > 0 and x > 0 and columns > x and D > z[o]:
                z[o] = D
                b[o] = chars[N if N > 0 else 0]

    if y_start == rows * y_separator - y_separator:
        y_start = 0

    for i in range(len(b)):
        A += 0.00002 # for faster rotation change to 0.0002
        B += 0.00001 # for faster rotation change to 0.0001
        if i == 0 or i % columns:
            text_display(b[i], x_start, y_start)
            x_start += x_separator
        else:
            y_start += y_separator
            x_start = 0
            text_display(b[i], x_start, y_start)
            x_start += x_separator


    pygame.display.update()

    hue += 0.005

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
#----------------------------------------------------------------------------------
# Tkinter example (can view corona project)
import tkinter as tk

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # create a prompt, an input box, an output label,
        # and a button to do the computation
        self.prompt = tk.Label(self, text="Enter a number:", anchor="w")
        self.entry = tk.Entry(self)
        self.submit = tk.Button(self, text="Submit", command = self.calculate)
        self.output = tk.Label(self, text="")

        # lay the widgets out on the screen.
        self.prompt.pack(side="top", fill="x")
        self.entry.pack(side="top", fill="x", padx=20)
        self.output.pack(side="top", fill="x", expand=True)
        self.submit.pack(side="right")

    def calculate(self):
        # get the value from the input widget, convert
        # it to an int, and do a calculation
        try:
            i = int(self.entry.get())
            result = "%s*2=%s" % (i, i*2)
        except ValueError:
            result = "Please enter digits only"

        # set the output widget to have our result
        self.output.configure(text=result)

# if this is run as a program (versus being imported),
# create a root window and an instance of our example,
# then start the event loop

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()

#==========================================================================
# Requests example
import requests
URL = "http://httpbin.org/ip"
def ipSearch():
    response =requests.get(URL)
    ip =response.json()['origin']
    return ip.split(",")[0]

if __name__=='__main__':
    print('Your IP is:', ipSearch())

# Geocoder example
import geocoder
g = geocoder.ip('199.7.157.0')
g = geocoder.ip('me')
print(g.latlng)
print(g.city)

