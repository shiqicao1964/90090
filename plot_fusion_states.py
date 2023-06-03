import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
from scipy.signal import butter, filtfilt

if __name__ == "__main__":
   
    
    x = np.genfromtxt('x.out',delimiter=',')
    y = np.genfromtxt('y.out',delimiter=',')
    phi = np.genfromtxt('phi.out',delimiter=',')

    keypoints = np.array([[-4.83,2.75],[-5.83,2.25],[-6.8,1.5],[-7.3,1.25],
                        [-8.33,2],[-8.33,4],[-8.33,6],[-8.33,8],[-8.33,8.75],[-7.35,9],[-6.35,9],
                        [-4.85,9],[-3.35,9],[-1.85,9],[-1.15,9],[-0.7,7.5],[-0.7,5.5],[-0.65,4],[-0.6,2.5],[-0.6,1], 
                        [-2.33,1],[-3.33,2.5],[-3.83,4]])

    num = len(x)
    #time.sleep(1000)

    fig2D = plt.figure(figsize = (12,12))
    ax1 = fig2D.add_subplot(2,2,1)
    ax2 = fig2D.add_subplot(2,2,2)
    ax3 = fig2D.add_subplot(2,2,3)
    ax4 = fig2D.add_subplot(2,2,4)

    t = np.linspace(0, num-1, num=num)

    ax1.plot(t,x,color='green')
    ax1.set_title('x')
    ax2.plot(t,y,color='green')
    ax2.set_title('y')
    

    ax4.plot(x,y,color='blue',label = 'recorded odomtery ')
    #ax4.plot(np.array([0,2]),np.array([0,0]),color='red',label = 'reference')
    ax4.plot(keypoints[:,0],keypoints[:,1],color='red',label = 'reference')
    ax4.scatter(keypoints[:,0],keypoints[:,1],c='red')
    ax4.set_xlabel('x [m]')
    ax4.set_ylabel('y [m]')
    ax4.legend()
    plt.show()
    import random
