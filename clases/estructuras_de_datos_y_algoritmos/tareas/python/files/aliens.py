#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
def readtxt(name="aliens.txt"):
	"""
	readtxt(name) , return txt content as array in safe mode 
        good practises make the master
	"""
	content = []
	with open(name, 'r') as file:
		for i in file.readlines():
			content.append(str(i).replace("\n",""))
	return content
def main():
    arr=readtxt("aliens.txt")
    alienñero=""
    value=0
    i=1
    while i<len(arr):
        if arr[i]>value:
                value=arr[i]
                alienñero=arr[i-1]
        i+=2
    return alienñero