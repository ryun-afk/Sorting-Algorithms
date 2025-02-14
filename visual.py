import numpy as np
import matplotlib.pyplot as plt

def plot(arr,delay=.01):
    n = len(arr)
    plt.bar(np.arange(0,n,1),arr)
    plt.pause(delay)
    plt.clf()