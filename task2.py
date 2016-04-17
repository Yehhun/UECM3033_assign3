

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt



def bio_system(y,t,a,b):
    y0 , y1 = y
    dydt = [a*(y0-y0*y1), b*(-y1+y0*y1)]
    return dydt

if __name__ == "__main__":
    a=1.0
    b=0.2
    initial_y0=0.1
    initial_y1=1.0
    initial_y=[initial_y0,initial_y1]
    
    # 100 partitions from 0 to 5    
    t = np.linspace(0,5,100)
    #non-linear ode system
    
    sol = odeint(bio_system,initial_y,t,args=(a, b))
    #sol=odeint(bio_system,initial_y,t,args=(a, b))

    #1303042
    # y0 and y1 against t
    
    plt.plot(t,sol[:,0],'b',label='y0 against t')
    plt.plot(t,sol[:,1],'c',label='y1 against t')
    plt.title('Graph y0 and y1 againt t with initial y0 = 0.1')    
    plt.xlabel('Year t')
    plt.ylabel('y')
    plt.legend(loc='best')
    plt.grid()
    plt.savefig('Graph_of_y0_and_y1_1.jpg')
    plt.show()
    
    # y1 against y0
    
    plt.plot(sol[:, 0],sol[:,1], 'b')
    plt.title('Graph of y1 against y0 with initial y0 = 0.1')
    plt.xlabel('y0')
    plt.ylabel('y1')
    plt.grid()
    plt.savefig('y1_against_y0_1.jpg')
    plt.show()

    # Part 2 
    a=1.0
    b=0.2
    initial_y0=0.11
    initial_y1=1.0
    initial_y=[initial_y0,initial_y1]
    t = np.linspace(0,5,100)
    sol=odeint(bio_system,initial_y,t,args=(a,b))
    
     # y0 and y1 against t 
    plt.plot(t, sol[:, 0], 'b', label='y0(t)')
    plt.plot(t, sol[:, 1], 'm', label='y1(t)')
    plt.title('Graph of y0 and y1 against t with initial y0 = 0.11')
    plt.xlabel('Year t') 
    plt.ylabel('y')
    plt.legend(loc='best')
    plt.grid()
    plt.savefig('Graph_of_y0_and_y1_11.jpg')
    plt.show()

    # y1 against y0 
    plt.plot(sol[:, 0],sol[:,1], 'r')
    plt.title('Graph of y1 against y0 with initial y0 = 0.11')
    plt.xlabel('y0')
    plt.ylabel('y1')
    plt.grid()
    plt.savefig('y1_against_y0_2.jpg')
    plt.show()
    
    