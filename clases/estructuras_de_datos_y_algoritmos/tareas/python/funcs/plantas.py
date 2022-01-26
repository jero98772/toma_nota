def plantavieja(arr):
 old=0
 name=""
 for i in arr:
  if i["antiguedad"] > old:
   old=i["antiguedad"]
   name=i["nombre"]
 print(name)
"""
nombre=input()
edad=int(input())
plantavieja(arr)
"""