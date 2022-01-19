def printSorted(arr, start, end):
    if start > end:
        return
     
    # print left subtree
    printSorted(arr, start * 2 + 1, end)
     
    # print root
    print(arr[start], end = " ")
     
    # print right subtree
    printSorted(arr, start * 2 + 2, end)
 
# Driver Code   
if __name__ == '__main__':
    arr = [3,9,29,4,11,17,51,3,8,10,12,15,20,37,88]
    arr_size = len(arr)3
    printSorted(arr, 0, arr_size - 1)


def PrintBST(node, BST):
    PrintBST(node.left)
    if node not empty:
        print(node_value)
    PrintBST(node.right)
    