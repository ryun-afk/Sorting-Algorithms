from visual import plot

# recursive sorting
# splits array in half
# repeat until arrays are too small (size 2 or 1)
# return two merged sorted arrays
# repeat until all arrays are merged

def merge(arr, left, mid, right):

    # initialize two sorted array
    n1 = mid - left + 1
    n2 = right - mid
    L = [0] * n1
    R = [0] * n2
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]


    # indexes
    i = 0 
    j = 0
    k = left

    # merging sorted arrays by comparing
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # adds other array to the end
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def recursive_merge_sort(arr, left, right ):
    if left < right:
        mid = (left + right) // 2

        plot(arr,1)

        recursive_merge_sort(arr, left, mid)
        recursive_merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def mergeSort(arr):
    print('Merge Sort')
    print(arr)
    recursive_merge_sort(arr,0,len(arr)-1)
    print(arr)