class Solution(object):
    def helper(self,root,ans):
        if root == None:
            return
        
        self.helper(root.left,ans)
        ans.append(root.val)
        self.helper(root.right,ans)    
    def inorderTraversal(self, root):
        ans=[]
        self.helper(root,ans)
        return ans
       

         