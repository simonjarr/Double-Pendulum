import numpy as np
from scipy.integrate import odeint
import time
from tkinter import *

i=0

# functions

# main render loop
def compute_render():
	global i
	# update angles
	theta_m1=out[i,0]
	theta_m2=out[i,2]

	# update line and mass coordinates
	xy2_Lm1=[width/2+L_1*np.sin(theta_m1),ceiling+L_1*np.cos(theta_m1)]
	myC.coords(l_m1,xy1_Lm1[0],xy1_Lm1[1],xy2_Lm1[0],xy2_Lm1[1])
	(x_m1,y_m1)=xy2_Lm1
	xy1_m1=[x_m1+r_m1,y_m1+r_m1]
	xy2_m1=[x_m1-r_m1,y_m1-r_m1]
	myC.coords(m1,xy1_m1[0],xy1_m1[1],xy2_m1[0],xy2_m1[1])
	xy2_Lm2=[x_m1+L_1*np.sin(theta_m2),y_m1+L_1*np.cos(theta_m2)]
	myC.coords(l_m2,xy2_Lm1[0],xy2_Lm1[1],xy2_Lm2[0],xy2_Lm2[1])
	(x_m2,y_m2)=xy2_Lm2
	xy1_m2=[x_m2+r_m2,y_m2+r_m2]
	xy2_m2=[x_m2-r_m2,y_m2-r_m2]
	myC.coords(m2,xy1_m2[0],xy1_m2[1],xy2_m2[0],xy2_m2[1])

	i+=1 # iterate

	if i==sim_time*10+1:
		sys.exit() # exit when the time comes

	root.after(10, compute_render) # update after 10 ms

# ode model
def model(y,t):
	theta1, theta1_d, theta2, theta2_d=y

	theta1_dd_n=-g*(2*m_1+m_2)*np.sin(theta1)-m_2*g*np.sin(theta1-2*theta2)-2*np.sin(theta1-theta2)*m_2*(theta2_d*theta2_d*L_2+theta1_d*theta1_d*L_1*np.cos(theta1-theta2))
	theta1_dd_d=L_1*(2*m_1+m_2-m_2*np.cos(2*theta1-2*theta2))

	theta2_dd_n=2*np.sin(theta1-theta2)*(theta1_d*theta1_d*L_1*(m_1+m_2)+g*(m_1+m_2)*np.cos(theta1)+theta2_d*theta2_d*L_2*m_2*np.cos(theta1-theta2))
	theta2_dd_d=L_2*(2*m_1+m_2-m_2*np.cos(2*theta1-2*theta2))

	theta1_dd=theta1_dd_n/theta1_dd_d
	theta2_dd=theta2_dd_n/theta2_dd_d

	dydt=[theta1_d,theta1_dd,theta2_d,theta2_dd]
	return dydt

# some constants
theta0=[3.14/6,0,3.14*60/180,0] # initial conditions

# canvas proportions
width=1280
height=720

# coordination computing
ceiling=height*1/5 # ceiling y location
l_ceiling=100 # ceiling x location
xy1_ceiling=[width/2-l_ceiling/2,ceiling]
xy2_ceiling=[width/2+l_ceiling/2,ceiling]
L_1=200 # length of line of mass 1
L_2=200 # length of line of mass 2
xy1_Lm1=[width/2,ceiling]
xy2_Lm1=[width/2+L_1*np.sin(theta0[0]),ceiling+L_1*np.cos(theta0[0])]
(x_m1,y_m1)=xy2_Lm1
xy1_Lm2=xy2_Lm1
xy2_Lm2=[x_m1+L_1*np.sin(theta0[2]),y_m1+L_1*np.cos(theta0[2])]
(x_m2,y_m2)=xy2_Lm2
r_m1=10 # radius of mass 1
r_m2=10 # radius of mass 2

# coordinates of mass 1 and 2
xy1_m1=[x_m1+r_m1,y_m1+r_m1]
xy2_m1=[x_m1-r_m1,y_m1-r_m1]
xy1_m2=[x_m2+r_m2,y_m2+r_m2]
xy2_m2=[x_m2-r_m2,y_m2-r_m2]

# physical constants
g=9.81 # gravitational constant
m_1=1  # mass of mass 1
m_2=10  # mass of mass 2

# simulation and dif eq. solving
real_time=100
sim_time=real_time*10
t = np.linspace(0, sim_time, (sim_time*10)+1) # create time array
out=odeint(model,theta0,t) # solve eq.

root =Tk() # set up root window

myC=Canvas(root,width=width,height=height, background="white") # create Canvas

line_ceiling=myC.create_line(xy1_ceiling,xy2_ceiling,fill="black",width="5") # create ceiling

l_m1=myC.create_line(xy1_Lm1,xy2_Lm1,fill="black",width="3") # create line of mass 1
l_m2=myC.create_line(xy1_Lm2,xy2_Lm2,fill="black",width="3") # create line of mass 2

m1=myC.create_oval(xy1_m1,xy2_m1, fill="black") # create mass 1
m2=myC.create_oval(xy1_m2,xy2_m2, fill="black") # create mass 2

myC.pack() # pack everything

root.after(10,compute_render) # update after 10 ms

root.mainloop() # run
