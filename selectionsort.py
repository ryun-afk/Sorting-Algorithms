
# traverse to find lowest element
# swaps element with correct location

def selectionSort(arr):
    n = len(arr)

    print(arr)

    min_index = 0
    for i in range(0,n-1):
        min_index = i
        for j in range(i,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    print(arr)
