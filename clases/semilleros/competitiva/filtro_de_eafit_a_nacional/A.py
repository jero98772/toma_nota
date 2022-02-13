def url2nums(url,ref):
    return url[url.index(ref)+len(ref):]
nn=int(input())
urlsValues=[]
urlStrPos="problemset/"
for i in range(nn):
    n,k=input().split(" ")
    #print(n,k)
    for ii in range(int(n)):
        urlsValues.append(int(url2nums(input(),urlStrPos)))
    urlsValues.sort()
    print(*urlsValues[:int(k)])
    urlsValues=[]

