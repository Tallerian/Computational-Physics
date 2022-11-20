from matplotlib.animation import FuncAnimation, writers
import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.animation as animation

#getting the length of the string
length = 1

arr = [[0,0,0]]

#parameters of the calculation
c = 1
c_der = 1
h = 1
delt_T = 1

#subdivide intervals
grid_space = 50
t = np.linspace(0, length, grid_space)
l_space = length/grid_space
size = len(t)
print("the size is ", size)


#initialisaing an list of tupples (0 = initial, 1 = prev, 2 = new state)

def initialiser(l):
    put = 0
    for i in range(l):
        if(i == 0):
            continue
        else:
            arr.append([0,0,0])
        put = (-200)*(pow((t[i]-0.5),2))
        put = pow(math.e,put)
        arr[i] = [put,put,put]
        #print("pos ",i, " has ", put)

#Now we define the leapfrog algorithm

def leapfrog(pos, l):
    
    #


    first = ((2*arr[pos][0])-(arr[pos][1]))
    #print("the pos ", pos, " size ",l)
    sec = (c/c_der)*((arr[pos+1][0]) + (arr[pos-1][0]) - (2*(arr[pos][0])))
    arr[pos][2] = first + sec

    


#now we have to updates the state of the position

def update(l):
    for pos in range(l):
        arr[pos][1] =  arr[pos][0]
        arr[pos][0] = arr[pos][2]


def graph_point(l):
    pty = [0]
    for i in range(l):
        if (i == 0):
            pty[i] = (arr[i][0])
        else:
            pty.append((arr[i][0]))

    return pty

dt = 0

#Display the figure
grid = plt.figure()
grid.set_figheight(5)
grid.set_figwidth(10)
plt.axis("equal")

initialiser(size)
ptyy = graph_point(size) ###The starting point of the string


def init_func():
    plt.clf()

def update_plot(i):
    plt.clf()
    for i in range(size):
        if (i == 0) or (i == size-1):
            pass
        else:
            leapfrog(i, size)   
    pty = graph_point(size)
    update(size)
    plt.plot(t, pty, 'k')
    plt.ylim([5,-5])
    plt.xlim([0,length])
    
anim = FuncAnimation(grid, update_plot, frames=400, init_func= init_func, interval=30)
anim.save('an3.gif', writer='Pillow', fps=20)
plt.show()    
