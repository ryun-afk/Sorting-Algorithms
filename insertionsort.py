from visual import plot

# compares and swap value positions
# inserts the element into the correct spot of an ordered array
# O(n^2)


def insertionSort(arr):
    print('Insertion Sort')
    print(arr)

    n = len(arr)
    for i in range(1,n):
        for j in range(0,i-1):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

        plot(arr)

    print(arr)