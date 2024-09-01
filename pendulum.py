import numpy as np
import matplotlib.pyplot as plt

angles = []
difference = []
for theta in range(0,3.14159, 0.1): 
    angles += theta
    difference += np.sin(theta) - theta

plt.scatter(angles,difference)

    