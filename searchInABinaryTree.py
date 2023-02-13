#700. Search in a Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root.val == val:
            return root
        elif val < root.val:
            if root.left:
                node = root.left
                return self.searchBST(node, val)
            else:
                return None
        else:
            if root.right:
                node = root.right
                return self.searchBST(node, val)
            else:
                return None
