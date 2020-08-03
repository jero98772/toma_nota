def bubbleSort(arr): 
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n): 
        print( n-i-1)
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
bubbleSort([1,3,5,6,7,8,9,2,4,6])