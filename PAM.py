import numpy as np
import matplotlib.pyplot as plt
from pylab import *

percent=50.0
TimePeriod=10.0 #Frozen Value Do not change
Cycles=10 #Frozen Value Do not change
dt=0.01 #Frozen Value Do not change

t=np.arange(0,Cycles*TimePeriod,dt);
pwm= t%TimePeriod<TimePeriod*percent/100

x=np.linspace(-10,10,10000) #Frozen Value Do not change
y=(np.sin(x))

y[(pwm =='False')] = 0      #Vectorisation for zero values
y[(pwm =='True')] = (y-pwm) # #Vectorisation for sine wave
plt.plot(t,y)

plt.ylim([-3,3])
plt.grid()
plt.show()
