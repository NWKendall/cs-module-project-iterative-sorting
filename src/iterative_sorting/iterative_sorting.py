# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # [A, B, C, | Z, Y, X]
    #  O, O, O, | U, U, U
    
    # loop through n-1 elements in arr
    for i in range(0, len(arr) - 1):
        cur_index = i # setting current index to variable, neccessary?
        smallest_index = cur_index # setting index with smallest val to var

        # for every i, loop ahead in same array
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        # Your code here
        # swapping the arrangement of i and j(smalles_index) if i isn't the smallest
        if smallest_index is not i:
            arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    for i in range (0, len(arr) -1 ):
        for j in range (0, len(arr) -1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr
