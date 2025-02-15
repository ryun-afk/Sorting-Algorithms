import numpy as np
from bubblesort import bubbleSort
from mergesort import mergeSort
from insertionsort import insertionSort
from selectionsort import selectionSort

amount = 20
min = 0 
max = 100

arr= np.random.randint(min,max,amount)
#bubbleSort(arr)

arr= np.random.randint(min,max,amount)
#mergeSort(arr)

arr= np.random.randint(min,max,amount)
insertionSort(arr)

arr= np.random.randint(min,max,amount)
#selectionSort(arr)