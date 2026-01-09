
from vpython import *
from random import random
import numpy as np
from collections import namedtuple
import math
G = 1
M = 1
R = 1

N = int(input("number of stars to simulate: "))
e = ((4/3*np.pi*(R**3))**1/3)/(N**1/3)
dt = 0.01
t = 0
def plummer_sphere(a=1.0):
    Xi = np.random.uniform(0, 1)
    
    r = a / np.sqrt(Xi**(-2/3) - 1)
    
    theta = np.arccos(np.random.uniform(-1, 1)) #polar angle
    phi = np.random.uniform(0, 2 * np.pi) #azimuthal angle
    
    #our actual coordinates 
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    
   
    v_esc = np.sqrt(2 * G * M / np.sqrt(r**2 + a**2))
    v_mag = 0
    q = 0.0

    while True:
        q = np.random.uniform(0, 1)
    
        g_q = 0.1 * np.random.uniform(0, 1)
        if g_q < (q**2 * (1 - q**2)**3.5):
            v_mag = q * v_esc
            break
    
    #random direction for velocity vector just like the coordiantes
    v_theta = np.arccos(np.random.uniform(-1, 1))
    v_phi = np.random.uniform(0, 2 * np.pi)
    
    vx = v_mag * np.sin(v_theta) * np.cos(v_phi)
    vy = v_mag * np.sin(v_theta) * np.sin(v_phi)
    vz = v_mag * np.cos(v_theta)

    return [[x,y,z], [vx,vy,vz]]


class Star:
    def __init__(self, pos,v):
        self.pos = pos
        self.v = v
        self.m = M / N
        self.p = self.m * self.v
        self.F = vector(0, 0, 0)
        self.a = self.F/self.m
        self.sphere = sphere(pos=self.pos, radius=R / 30, make_trail=True, retain=100, color = vector(random(), random(), random()))
    
    def update_position(self, dt):
        self.pos += self.v * dt 
        self.sphere.pos = self.pos

    def update_vel(self,dt):
        self.v += self.a * dt/2

def calc_forces():
    for star in stars:
        star.F = vector(0, 0, 0)

    for i in range(len(stars)):
        for j in range(len(stars)):
            if i != j:
                rji = stars[j].pos - stars[i].pos
                dist = mag(rji)
                stars[i].F += G * stars[i].m * stars[j].m * norm(rji) / math.pow((dist**2 + e**2),3/2)
                stars[j].F -= G * stars[i].m * stars[j].m * norm(rji) / math.pow((dist**2 + e**2),3/2)
                

#Initialize stars list
stars = []
for _ in range(N):
    data = plummer_sphere() 
    rt = vector(*map(float, data[0]))
    v = vector(*map(float, data[1]))
    stars.append(Star(rt, v))

while t < 10:
    rate(100)
    
    #Update positions
    for star in stars:
        star.update_vel(dt)
    for star in stars:
        star.update_position(dt)
    calc_forces()
    for star in stars:
        star.update_vel(dt)

    t += dt
