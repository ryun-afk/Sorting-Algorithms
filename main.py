import numpy as np
from bubblesort import bubbleSort
from mergesort import mergeSort
from insertionsort import insertionSort

amount = 20
arr= np.random.randint(0,100,amount)
#bubbleSort(arr)

arr= np.random.randint(0,100,amount)
#mergeSort(arr)

arr= np.random.randint(0,100,amount)
insertionSort(arr)
