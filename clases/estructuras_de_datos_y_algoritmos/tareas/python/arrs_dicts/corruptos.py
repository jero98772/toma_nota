def mascorrupto(arr):
    name=""
    value=0
    i=1
    while i<len(arr):
        if arr[i]>value:
                value=arr[i]
                name=arr[i-1]
        i+=2
    return name