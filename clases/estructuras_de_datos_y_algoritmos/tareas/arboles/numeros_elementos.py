#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#chimba de nombre con Ñ


def TamañoArbol( root):
    if not root:
        return 0
    else:
        return (TamañoArbol(root.left)+ 1 + TamañoArbol(root.right))
    #return root.TamañoArbolaux(0)
        