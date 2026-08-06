# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
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
            for i in range(sz):
                cur=q.popleft()
                if i == sz -1:
                    l.append(cur.val)
                if cur.left != None:
                    q.append(cur.left)
                if cur.right != None:
                    q.append(cur.right)
            
        return l
             
        
        