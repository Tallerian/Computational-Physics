from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
import random

#Radius
R = 20

#maximum velocity
max_v = 5/R
#dawdle probability
p = 0.6

#Number of cars 
N = 4

# Make an array of lists storing car states
# the 1st stores the x position of the cell, 2nd y position of the cell, and 3rd the velocity
cars = [[]]


#function dist returns the distance btn a car and the next one
def dist(car_next, car_rn):
    #strt = math.sqrt((R*(car_next[0]-car_rn[0])**2)+((R*(car_next[1]-car_rn[1])**2)))
    angle = np.cos(car_next[0]) - np.cos(car_rn[0])
    if (angle < 0):
        angle = 2+angle
    distance = (angle*np.pi)*R
    return distance


ptx = [0]
pty = [0]

#Function for point initialisation
def point_init(arr, num):
    for i in range(num):
        ptx[i] = R*np.cos(arr[i][0]) 
        pty[i] = R*np.sin(arr[i][1])


def point_def(pointx, pointy, velocity):
    temp = [pointx, pointy,velocity]
    return temp


cars[0] = (point_def(0.4, 0.4, 1/R)) 
cars.append(point_def(0.8, 0.8, 1/R))
cars.append(point_def(1.2, 1.2, 1/R))
cars.append(point_def(1.6, 1.6, 1/R))
cars.append(point_def(1.8, 1.8, 1/R))
""" cars.append(point_def(2.6, 2.6, 1/R))
cars.append(point_def(2.9, 2.9, 1/R))
cars.append(point_def(3.4, 3.4, 1/R)) """


#defining a function to append cars in the circle
def add_cars(num):
    for i in range(num):
        frst = random.uniform(0.00,6.28)
        frst = round(frst,2)
        velocity = random.uniform(0,1)
        velocity = round(velocity,2)
        cars.append(point_def(frst, frst, velocity/R))
    return num

#arraning cars according to points
def arrange(num):
    a = 0
    i = 0
    while i < num-1:
        if (cars[i][0]>cars[i+1][0]):
            temp = cars[i][0]
            cars[i][0] = cars[i+1][0]
            cars[i][1] = cars[i+1][1]
            cars[i+1][0] = temp
            cars[i+1][1] = temp
            i = -1
        i = i + 1
        a = a + 1

#dawdle_probabilty
def dawdle(lim):
    check = random.uniform(0.00,1.00)
    if check == 0:
        return 0
    if (check <= lim):
        return 1
    else:
        return 0

#next step function
def next_step(num):
    for i in range(num):
        #1st check
        if cars[i][2] < max_v:
            if i == num-1:
                cars[i][2] = round((cars[i][2] + 1/R),2)
            else:
                cars[i][2] = round((cars[i][2] + 1/R),2)

        #2nd check
        if i == num-1:
            #print(cars[0]," ", cars[i])
            distance = dist(cars[0], cars[i])
            """ print("the distance is ", distance) """
        else:
            #print(cars[i+1]," ", cars[i])
            distance = dist(cars[i+1], cars[i])
        if distance < cars[i][2]:
            cars[i][2] = round(distance/R,2) - 0.000001

        #3rd check with dawdle probability
        check = dawdle(p)
        if(check == 1):
            cars[i][2] = cars[i][2] - 1/R
        

def next_place(num):
    for i in range(num):
        cars[i][0] = cars[i][0] + (cars[i][2]/R)
        cars[i][1] = cars[i][1] + (cars[i][2]/R)


def pt_init(num):
    for i in range(num-1):
        ptx.append(0)
        pty.append(0)


#number of edges
n = 64

#number of edges
n = 64

#subdivide intervals
t = np.linspace(0, 2*np.pi, n+1)


#x and y arrays of the points on the ring path for the cars
x = R*np.cos(t)
y = R*np.sin(t)

#Display the circle
grid = plt.figure()
plt.axis("equal")

#initialising all cars and points before looping the motion
N = N + add_cars(15)
arrange(N)
pt_init(N)



def init_func():
    plt.clf()

def update_plot(i):
    plt.clf()
    point_init(cars, N)
    plt.plot(x, y, 'k')
    plt.scatter(ptx, pty, 15)
    text = "Time t = "+ str(i)+ "s"
    grid.text(0.45,0.50, text)
    next_step(N)
    next_place(N)

anim = FuncAnimation(grid, update_plot, frames=np.linspace(1, 1000, 1000), init_func= init_func, interval=30)
#anim.save("part_a.mp4", dpi=150, fps = 30, writer='ffmpeg')
plt.show()
