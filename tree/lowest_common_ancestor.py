class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:     #if p val and q val are both greater than root value, go down right subtree
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val    # if both values are less, go down left subree
                cur = cur.left
            else:                                       # result found
                return cur

