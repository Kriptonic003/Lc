# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        q=deque()
        if root is not None:
            q.append(root)
        else:
            return []
        count=0   
        l=[]   
        while q:
            sz=len(q)
            r=[]
            for _ in range(sz):
                cur=q.popleft()
                r.append(cur.val)
                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)
            if count%2==0:
                l.append(r)
            else:
                l.append(r[::-1]) 
            count+=1
        return l                             

        