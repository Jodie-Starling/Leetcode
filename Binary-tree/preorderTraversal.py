#leetcode 144 二叉树的前序遍历

'''
# 递归
时间复杂度：O(n)
空间复杂度：O(h) h为树的高度
'''
# 前序遍历-递归-LC144_二叉树的前序遍历
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        def dfs(node):  # dfs Depth-First Search, 深度优先搜索
            if node is None:
                return
            
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return res
    


'''
# 迭代
时间复杂度：O(n)
空间复杂度：O(h) h为树的高度
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        stack = [root]
        res = []

        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return res