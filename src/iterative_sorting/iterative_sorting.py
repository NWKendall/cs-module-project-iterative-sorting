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
# https://www.geeksforgeeks.org/counting-sort/
def count_sort(arr, maximum=-1):
    # counts number of times each character appears in array
    # sorts them by frequency?
    # Your code here

    # output character array containing sorted arr
    output = [0 for i in range(maximum)]
    
    # create count array to store count for each value
    count = [0 for i in range(maximum)]

    
    # For storing the resulting answer since the  
    # string is immutable 
    ans = ["" for _ in arr]

    # store count of each character
    for i in arr:
        count[ord(i)] += 1
    
    # Change count[i] so that count[i] now contains actual 
    # position of this character in output array 
    for i in range(maximum):
        count[i] += count[i-1]
    
    # Build the output character array 
    for i in range(len(arr)):
        output[count[ord(arr[i])]-1] = arr[i]
        count[ord(arr[i])] -= 1

    # Copy the output array to arr, so that arr now 
    # contains sorted characters 
    for i in range(len(arr)):
        ans[i] = output[i]
    return ans




ar = "geeksforgeeks"

ans = count_sort(ar, 256)
print("".join(ans))
