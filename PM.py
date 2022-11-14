import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def sin_wave(amp, freq, time):
    return amp * np.sin(2*np.pi*freq*time)
def pulse_wave(amp, freq, sample):
    #return np.arange(sample) % period < width
    p = amp * signal.square(2 * np.pi * freq * time)
    for i in range(len(p)):
        if p[i] < 0:
            p[i] = 0
    return p

if __name__ == '__main__':
    #time = np.arange(0, 0.1, 0.0001)
    time = np.linspace(0, 0.002, 5000)
    sin1 = sin_wave(1, 10000, time)
    pulse = pulse_wave(1, 1000, time)

    mod = sin1 * pulse


    plt.subplot(3, 1, 1)
    plt.ticklabel_format(axis='x', style='sci', scilimits=(0,1), useMathText=True)
    plt.plot(time, sin1)

    plt.subplot(3, 1, 2)
    plt.ticklabel_format(axis='x', style='sci', scilimits=(0, 1), useMathText=True)
    plt.plot(time, pulse)

    plt.subplot(3, 1, 3)
    plt.ticklabel_format(axis='x', style='sci', scilimits=(0, 1), useMathText=True)
    plt.plot(time, mod)

    #plt.ylim(-2, 2)

    plt.show()
