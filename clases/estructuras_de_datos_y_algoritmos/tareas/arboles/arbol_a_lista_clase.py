def ArbolALista(root: Node) -> None:
    if root == None:
        return
    else:
        temp = root.right
        root.right = root.left
        root.left = None
        ArbolALista(root.right)