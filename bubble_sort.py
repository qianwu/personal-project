### bubble sort algorithm
### bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j + 1] = arr[j+1], arr[j]
    
arr = [5,2,8,4,1]
bubble_sort(arr)
print(arr)
