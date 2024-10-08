import numpy as np

g = 9.8
L =2
mu =0.2
theta_0 = np.pi/3
theta_dot = 0

def get_double_dot(theta,theta_dot):
    return -mu *theta_dot - (L/g) * np.sin(theta)

def theta(t):
    time_interval = 0.01
    for time in np.arrange(0,t,time_interval):
        theta_0 += theta_dot * time_interval
        theta_dot = get_double_dot(theta_0,theta_dot)
    return theta_0

for i in range(10,0,2): 
    print(i)