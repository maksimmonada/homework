import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def whale():
    x1 = np.arange(0, 9, 0.01)
    x2 = np.arange(-10, 0, 0.01)
    x3 = np.arange(-9, -3, 0.01)
    x4 = np.arange(-3, 9, 0.01)
    x5 = np.arange(5, 8.3, 0.01)
    x6 = np.arange(5, 8.5, 0.01)
    x7 = np.arange(-13, -9, 0.01)
    x8 = np.arange(-15, -13, 0.01)
    x9 = np.arange(-15, -10, 0.01)
    x10 = np.arange(3, 4, 0.01)
    y1 = (2/27*(x1**2) - 3)
    y2 = (0.04*(x2**2) - 3)
    y3 = (2/9*((x3+6)**2) + 1)
    y4 = (-1/12*((x4-3)**2) + 6)
    y5 = (1/9*((x5-5)**2) + 2)
    y6 = (1/8*((x6-7)**2) + 1.5)
    y7 = (-0.75*((x7+11)**2) + 6)
    y8 = (-0.5*((x8+13)**2) + 3)
    y9 = [1] * len(x9)
    y10 = [3] * len(x10)
   
    plt.subplots()
    plt.grid(True)

    plt.plot(x1,y1 ,':g',linewidth=1)
    plt.plot(x2,y2 ,':g',linewidth=1)
    plt.plot(x3,y3 ,':g',linewidth=1)
    plt.plot(x4,y4 ,':g',linewidth=1)
    plt.plot(x5,y5 ,':g',linewidth=1)
    plt.plot(x6,y6 ,':g',linewidth=1)
    plt.plot(x7,y7 ,':g',linewidth=1)
    plt.plot(x8,y8 ,':g',linewidth=1)
    plt.plot(x9,y9 ,':g',linewidth=1)
    plt.plot(x10,y10 ,':g',linewidth=1)


    plt.savefig("my_image.png")
    plt.show()

def glasses():
    x1 = np.arange(-9, -1, 0.01)
    y1 = (-0.0625*((x1+5)**2) + 2)
    x2 = np.arange(1, 9, 0.01)
    y2 = (-0.0625*((x2-5)**2) + 2)
    x3 = np.arange(-9, -1, 0.01)
    y3 = (0.25*((x3+5)**2) - 3)
    x4 = np.arange(1, 9, 0.01)
    y4 = (0.25*((x4-5)**2) - 3)
    x5 = np.arange(-9, -6,  0.01)
    y5 = (-((x5+7)**2) + 5)
    x6 = np.arange(6, 9, 0.01)
    y6 = (-((x6-7)**2) + 5)
    x7 = np.arange(-1, 1, 0.01)
    y7 = (-0.5*(x7**2) + 1.5)

    plt.subplots()
    plt.grid(True)

    plt.plot(x1,y1 ,'--o',linewidth=1)
    plt.plot(x2,y2 ,'--o',linewidth=1)
    plt.plot(x3,y3 ,'--o',linewidth=1)
    plt.plot(x4,y4 ,'--o',linewidth=1)
    plt.plot(x5,y5 ,'--o',linewidth=1)
    plt.plot(x6,y6 ,'--o',linewidth=1)
    plt.plot(x7,y7 ,'--o',linewidth=1)

    plt.savefig("my_image.png")
    plt.show()

def umbrella():
    x1 = np.arange(-12, 12, 0.02)
    y1 = (-1/18*(x1**2) + 12)
    x2 = np.arange(-4, 4, 0.02)
    y2 = (-1/8*(x2**2) + 6)
    x3 = np.arange(-12, -4, 0.02)
    y3 = (-1/8*((x3+8)**2) + 6)
    x4 = np.arange(4, 12, 0.02)
    y4 = (-1/8*((x4-8)**2) + 6)
    x5 = np.arange(-4, -0.3, 0.02)
    y5 = (2*((x5+3)**2) - 9)
    x6 = np.arange(-4, 0.2, 0.02)
    y6 = (1.5*((x6+3)**2) - 10)

    plt.subplots()
    plt.grid(True)

    plt.plot(x1,y1 ,'--m',linewidth=1)
    plt.plot(x2,y2 ,'--m',linewidth=1)
    plt.plot(x3,y3 ,'--m',linewidth=1)
    plt.plot(x4,y4 ,'--m',linewidth=1)
    plt.plot(x5,y5 ,'--m',linewidth=1)
    plt.plot(x6,y6 ,'--m',linewidth=1)

    plt.savefig("my_image.png")
    plt.show()

def butterfly():
    x1 = np.arange(-9, -1, 0.02)
    x2 = np.arange(1, 9, 0.02)
    x3 = np.arange(-9, -8, 0.02)
    x4 = np.arange(8, 9, 0.02)
    x5 = np.arange(-8, -1, 0.02)
    x6 = np.arange(1, 8, 0.02)
    x7 = np.arange(-8, -1, 0.02)
    x8 = np.arange(1, 8, 0.02)
    x9 = np.arange(-8, -2, 0.02)
    x10 = np.arange(2, 8, 0.02)
    x11 = np.arange(-2, -1, 0.02)
    x12 = np.arange(1, 2, 0.02)
    x13 = np.arange(-1, 1, 0.02)
    x14 = np.arange(-1, 1, 0.02)
    x15 = np.arange(-2, 0, 0.02)
    x16 = np.arange(0, 2, 0.02)
    y1 = (-1/8*((x1+9)**2) + 8)
    y2 = (-1/8*((x2-9)**2) + 8)
    y3 = (7*((x3+8)**2) + 1)
    y4 = (7*((x4-8)**2) + 1)
    y5 = (1/49*((x5+1)**2))
    y6 = (1/49*((x6-1)**2))
    y7 = (-4/49*(x7+1)**2)
    y8 = (-4/49*(x8-1)**2)
    y9 = (1/3*((x9+5)**2) -7)
    y10 = (1/3*((x10-5)**2) -7)
    y11 = (-2*((x11+1)**2) -2)
    y12 = (-2*((x12-1)**2) -2)
    y13 = (-4*(x13**2) + 2)
    y14 = (4*(x14**2) - 6)
    y15 = ((-1.5*x15) +2)
    y16 = ((1.5*x16) +2)

    plt.subplots()
    plt.grid(True)

    plt.plot(x1,y1 ,'--b',linewidth=1)
    plt.plot(x2,y2 ,'--b',linewidth=1)
    plt.plot(x3,y3 ,'--b',linewidth=1)
    plt.plot(x4,y4 ,'--b',linewidth=1)
    plt.plot(x5,y5 ,'--b',linewidth=1)
    plt.plot(x6,y6 ,'--b',linewidth=1)
    plt.plot(x7,y7 ,'--b',linewidth=1)
    plt.plot(x8,y8 ,'--b',linewidth=1)
    plt.plot(x9,y9 ,'--b',linewidth=1)
    plt.plot(x10,y10 ,'--b',linewidth=1)
    plt.plot(x11,y11 ,'--b',linewidth=1)
    plt.plot(x12,y12 ,'--b',linewidth=1)
    plt.plot(x13,y13 ,'--b',linewidth=1)
    plt.plot(x14,y14 ,'--b',linewidth=1)
    plt.plot(x15,y15 ,'--b',linewidth=1)
    plt.plot(x16,y16 ,'--b',linewidth=1)


    plt.savefig("my_image.png")
    plt.show()

def frog():
    x1 = np.arange(-7, 7, 0.01)
    x2 = np.arange(-7, 7, 0.01)
    x3 = np.arange(-6.8, -2, 0.01)
    x4 = np.arange(2, 6.8, 0.01)
    x5 = np.arange(-5.8, -2.8, 0.01)
    x6 = np.arange(2.8, 5.8, 0.01)
    x7 = np.arange(-4, 4, 0.01)
    x8 = np.arange(-5.2, 5.2, 0.01)
    x9 = np.arange(-7, -2.8, 0.01)
    x10 = np.arange(2.8, 7, 0.01)
    x11 = np.arange(-7, 0, 0.01)
    x12 = np.arange(0, 7, 0.01)
    x13 = np.arange(-7, -4.5, 0.01)
    x14 = np.arange(4.5, 7, 0.01)
    x15 = np.arange(-3, 3, 0.01)
    y1 = ((-3/49)*(x1**2)) + 8
    y2 = ((4/49)*(x2**2)) + 1
    y3 = (-0.75*(x3+4)**2) + 11
    y4 = (-0.75*(x4-4)**2) + 11
    y5 = (-((x5+4)**2)) +9
    y6 = (-((x6-4)**2)) +9
    y7 = ((4/9)*(x7**2)) -5
    y8 = ((4/9)*(x8**2)) -9
    y9 = (-1/16*(x9+3)**2) -6
    y10 = (-1/16*(x10-3)**2) -6
    y11 = (1/9*(x11+4)**2) -11
    y12 = (1/9*(x12-4)**2) -11
    y13 = (-(x13+5)**2)
    y14 = (-(x14-5)**2)
    y15 = (2/9*(x15**2)) +2

    plt.subplots()
    plt.grid(True)

    plt.plot(x1,y1 ,'--c',linewidth=1)
    plt.plot(x2,y2 ,'--c',linewidth=1)
    plt.plot(x3,y3 ,'--c',linewidth=1)
    plt.plot(x4,y4 ,'--c',linewidth=1)
    plt.plot(x5,y5 ,'--c',linewidth=1)
    plt.plot(x6,y6 ,'--c',linewidth=1)
    plt.plot(x7,y7 ,'--c',linewidth=1)
    plt.plot(x8,y8 ,'--c',linewidth=1)
    plt.plot(x9,y9 ,'--c',linewidth=1)
    plt.plot(x10,y10 ,'--c',linewidth=1)
    plt.plot(x11,y11 ,'--c',linewidth=1)
    plt.plot(x12,y12 ,'--c',linewidth=1)
    plt.plot(x13,y13 ,'--c',linewidth=1)
    plt.plot(x14,y14 ,'--c',linewidth=1)
    plt.plot(x15,y15 ,'--c',linewidth=1)


    plt.savefig("my_image.png")
    plt.show()

def diagram():
    fail=open("Andmed.txt","r")
    mas1=[]
    mas2=[]
    for line in fail:
        n=line.find(",")
        mas1.append(line[0:n].strip())
        mas2.append(int(line[n+1:len(line)].strip()))
    fail.close()

    title = "Dann6e IT security"
    plt.grid(True)
    color_rectangle = ["r", "g", "m", "b"]
    plt.barh(mas1, mas2, color=color_rectangle)
    plt.show()

glasses()
umbrella()
butterfly()
whale()
frog()
diagram()
