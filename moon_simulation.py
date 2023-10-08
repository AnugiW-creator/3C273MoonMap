# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 19:58:24 2023

@author: Yi Gan
"""
import visualpython as visual
import plotly.express as px
import vector
import vpython
from vpython import sphere
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import animation
from matplotlib.animation import FuncAnimation
#%%

"""
create a sphere with spherical coordinates, and animate the sphere
"""
radius = 3
theta = np.linspace(0,2*np.pi,100)
phi = np.linspace(0, np.pi, 100)

x = radius*np.outer(np.cos(theta),np.sin(phi))
y = radius*np.outer(np.sin(theta),np.sin(phi))
z = radius*np.outer(np.ones(np.size(theta)), np.cos(phi))

#fig = plt.figure()
#ax = plt.axes(projection = '3d')
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(x,y,z, color='cyan')
ax.set_title("A Sphere!")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_facecolor('w')


#ax.set_box_aspect([1,1,1])

def init():
    ax.plot_surface(x, y, z,antialiased=False)
    return fig

#animate
def animate(i):
    ax.view_init(elev = 20, azim = i*4)
    return fig

ani = animation.FuncAnimation(fig, animate, init_func=init, frames = 100, interval = 200)

plt.axis('off')
plt.show()

#%%

"""
create a sphere with moon image
"""

from PIL import Image
im = Image.open('lroc_color_poles_2k.jpg')
#im.show()  #check if the image is imported successfully

im = np.array(im.resize([d/1 for d in im.size]))/256

long = np.linspace(-180, 180, im.shape[1]) * np.pi/180  #longitude in degree
lat = np.linspace(-90, 90, im.shape[0])[::-1] * np.pi/180  #latitude in degree
rad = 10 #radius of the moon

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


#x = rad*np.outer(np.cos(long), np.sin(lat)) #
#y = rad*np.outer(np.sin(long), np.sin(lat))
#z = rad*np.outer(np.ones(np.size(long)), np.cos(lat))

x = rad*np.outer(np.cos(long), np.cos(lat)).T #
y = rad*np.outer(np.sin(long), np.cos(lat)).T
z = rad*np.outer(np.ones(np.size(long)), np.sin(lat)).T
#ax.plot_surface(x, y, z, rstride=4, cstride=4, facecolors = im, antialiased=False)

"""
To make the 'moon' rotates
"""
plt.axis('off')
def init():
    ax.plot_surface(x, y, z,rstride=4, cstride=4, facecolors = im, antialiased=False)
    return fig

#animate
def animate(i):
    ax.view_init(elev = 20, azim = i*4)
    return fig

ani = animation.FuncAnimation(fig, animate, init_func=init, frames = 100, interval = 200)

lat_station, long_station = np.loadtxt('station_location.csv',
                                       delimiter=',',skiprows= 1, usecols=[4,5], unpack= True) #Apollo stations
A,  lat, lat_err, long, long_err, dep, dep_err = np.loadtxt('nakamura_2005_dm_locations.csv', skiprows=1,
                                                            delimiter=',',usecols=[0,2,3,4,5,6,7] , unpack=True) #moonquake in 2005
year_1979 , d_1979, lat_1979, long_1979, mag_1979= np.loadtxt('nakamura_1979_sm_locations_edited.csv', delimiter =',', 
                                                              skiprows=1, usecols=[0,1,5,6,7], unpack=True) #moon quake in 1979

x0 = []
y0 = []
z0 = []
x_station = [] #coordinates of the stations
y_station = []
z_station = []
r = 10.2

ax.scatter(x_station, y_station, z_station, marker='X', c = 'r', s=10) #plot the Apollo stations on the sphere
for i in range(len(lat)):
    lat_p = lat[i]
    long_p = long[i]
    x_p = r * np.cos(long_p) * np.sin(lat_p)
    y_p = r * np.sin(long_p) * np.sin(lat_p)
    z_p = r * np.cos(lat_p)
    #print(x_p, y_p, z_p)
    x0.append(x_p)
    y0.append(y_p)
    z0.append(z_p)
    plt.pause(1)
    ax.scatter(x0, y0, z0, marker='o', c = 'white', s=10)
    
for i in range(len(lat_station)):
    lat_s = lat_station[i]
    long_s = long_station[i]
    x_s = r * np.cos(long_s) * np.sin(lat_s)
    y_s = r * np.sin(long_s) * np.sin(lat_s)
    z_s = r * np.cos(lat_s)
    #print(x_p, y_p, z_p)
    x_station.append(x_s)
    y_station.append(y_s)
    z_station.append(z_s)

#print(len(x0), len(y0), len(z0))

x_1979 = []
y_1979 = []
z_1979 = []
r = 10.3
t = []

for i in range(len(lat_1979)):
    lat_s = lat_1979[i]
    long_s = long_1979[i]
    x_s = r * np.cos(long_s) * np.sin(lat_s)
    y_s = r * np.sin(long_s) * np.sin(lat_s)
    z_s = r * np.cos(lat_s)
    #print(x_p, y_p, z_p)
    x_1979.append(x_s)
    y_1979.append(y_s)
    z_1979.append(z_s)
    
    plt.pause(1)
    ax.scatter(x_1979, y_1979, z_1979, marker='o', c = 'b', s=10)



plt.show()

#%%
