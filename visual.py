import numpy as np
import matplotlib.pyplot as plt

def plot(arr):
    n = len(arr)
    plt.bar(np.arange(0,n,1),arr)
    plt.pause(0.01)
    plt.clf()