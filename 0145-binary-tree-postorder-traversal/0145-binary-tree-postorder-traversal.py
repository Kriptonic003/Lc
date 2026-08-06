class Solution(object):
    def helper(self,root,ans):
        if root == None:
            return
        
        self.helper(root.left,ans)
        self.helper(root.right,ans)  
        ans.append(root.val)  
    def postorderTraversal(self, root):
        ans=[]
        self.helper(root,ans)
        return ans
       

         