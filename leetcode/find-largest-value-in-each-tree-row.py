# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def largestValues(root):
    def traverse(root, level, arr):  
        if root is None:
            return 
        if len(arr) == level:
            arr.append(root.val)
        else:
            arr[level] = max(root.val, arr[level])
        traverse(root.left, level +1, arr)
        traverse(root.right, level +1, arr)

    if root is None:
        return None
    arr = []
    traverse(root, 0, arr)
    return arr

T = TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(9)), TreeNode(2, None, TreeNode(9)))

print(largestValues(T))
