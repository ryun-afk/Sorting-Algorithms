from visual import plot

# recursive algorithm
# divides array into higher or lower than pivot
# repeats for higher and lower partitions

def recursive_quick_sort(arr, start, end):
    if start < end:
        index = start
        for i in range(start,end):
            if arr[i] < arr[end]:
                arr[index], arr[i] = arr[i], arr[index]
                index = index + 1
        plot(arr)
        arr[index],arr[end] = arr[end], arr[index]
        recursive_quick_sort(arr,start,index-1)
        recursive_quick_sort(arr,index+1,end)

def quickSort(arr):
    print('Quick Sort')
    print(arr)

    recursive_quick_sort(arr,0,len(arr)-1)
    print(arr)
