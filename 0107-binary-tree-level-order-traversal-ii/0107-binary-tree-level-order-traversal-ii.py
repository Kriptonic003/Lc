# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        q=deque()
        if root !=None:
            q.append(root)
        else:
            return  [] 
        l=[]
        while len(q)>0:
            sz=len(q)
            row=[]
            for _ in range(sz):
                cur=q.popleft()
                
                row.append(cur.val)
                if cur.left != None:
                    q.append(cur.left)
                if cur.right != None:
                    q.append(cur.right)
            l.append(row)
        return l[::-1]
        