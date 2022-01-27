def mascorrupto(arr):
    name=""
    value=""
    for i in range(len(arr)):
        if i%2==0:
            if value>arr[i]:
                value=arr[i]
                name=arr[i-1]
    print(name)