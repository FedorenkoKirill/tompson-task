#!/usr/bin/env python3
import time
start_time = time.time()
import math
import random
import matplotlib.pyplot as plt
import numpy as np

#k=9*(10**9)
k=1
#e=1.60217662*(10**-19)
e=1
#R=53*(10**-12)
R=1

def get_charges(n):
    charge_list=list()
    for i in range(n):
        x=random.randint(-100,100)/100
        y=random.randint(-100,100)/100
        z=random.randint(-100,100)/100
        r=math.sqrt(x*x+y*y+z*z)
        x=x/r*R
        y=y/r*R
        z=z/r*R
        charge=np.array([[x],[y],[z]])
        charge_list.append(charge)
    return charge_list

def force(v1, l):
    resultant=list()
    for v2 in range(len(l)):
        r=math.sqrt((v1[0]-l[v2][0])**2+(v1[1]-l[v2][1])**2+(v1[2]-l[v2][2])**2)
        F=(k*e*e)/(r*r)
        v=(l[v2]-v1)*(-1)*F
        resultant.append(v)
    v=0
    for i in resultant:
        v+=i
    v+=v1
    r=math.sqrt((v[0][0])**2+(v[1][0])**2+(v[2][0])**2)
    v=v/r*R
    return v

def get_energy(l):
    W=0
    for i in range(len(l)-1):
        for ii in range(i,len(l)):
            if i!=ii:
                r=math.sqrt((l[i][0]-l[ii][0])**2+(l[i][1]-l[ii][1])**2+(l[i][2]-l[ii][2])**2)
                W+=k*e*e/r
    return W

def plotting_points(ax,color,charge_list):
    for v in charge_list:
        x=v[0][0]
        y=v[1][0]
        z=v[2][0]
        ax.scatter(x,y,z,c=color,s=70,depthshade=True)

def draw_sphere(ax):
    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x = R*np.cos(u)*np.sin(v)
    y = R*np.sin(u)*np.sin(v)
    z = R*np.cos(v)
    ax.plot_wireframe(x, y, z, color="grey")
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

def get_results_vectors(l):
    W=1;W0=0
    while W-W0!=0:
        W0=get_energy(l)
        for v1 in range(len(l)):
            new_list=list()
            for i in range(len(l)):
                if i!=v1:
                    new_list.append(l[i])
            v=force(l[v1],new_list)
            l[v1]=v
        W=get_energy(l)
    return l 

if __name__ == "__main__":
    n = int(input('Введите число точек на сфере:   '))
    fig=plt.figure()
    ax=fig.add_subplot(111, projection='3d')
    blue_list=get_charges(n)
    green_list=get_results_vectors(blue_list)
    plotting_points(ax,'blue',green_list)
    draw_sphere(ax)
    plt.show()

