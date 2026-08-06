class Solution(object):
    def helper(self,root,ans):
        if root == None:
            return
        ans.append(root.val)
        self.helper(root.left,ans)
        self.helper(root.right,ans)    
    def preorderTraversal(self, root):
        ans=[]
        self.helper(root,ans)
        return ans
       

         