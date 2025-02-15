import numpy as np
import matplotlib.pyplot as plt

def plot(arr,delay=.1):
    n = len(arr)
    plt.bar(np.arange(0,n,1),arr)
    plt.pause(delay)
    plt.clf()