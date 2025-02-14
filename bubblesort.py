from visual import plot

def bubbleSort(arr):
    print('Bubble Sort')
    print(arr)
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):

            # plot visual
            plot(arr)

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)