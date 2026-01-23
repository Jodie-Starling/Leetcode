#leetcode 145 二叉树的后序遍历
'''
# 递归
时间复杂度：O(n)，其中 n 是二叉树的节点个数。每个节点恰好被访问一次。
空间复杂度：O(h)，其中 h 是二叉树的高度。主要为递归调用栈的开销，最坏情况下树呈现链状，空间复杂度为 O(n)；平均情况下树的高度与节点数的对数成正比，空间复杂度为 O(log n)。
'''

# 后序遍历-递归-LC145_二叉树的后序遍历
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        def dfs(node):
            if node is None:
                return
            
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)

        dfs(root)
        return res
    


'''
# 迭代
时间复杂度：O(n)，其中 n 是二叉树的节点个数。每个节点恰好被访问一次。
空间复杂度：O(n)，其中 n 是二叉树的节点个数。主要为栈的开销，最坏情况下树呈现链状，空间复杂度为 O(n)；平均情况下树的高度与节点数的对数成正比，空间复杂度为 O(log n)。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        stack = [root]
        res = []

        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return res[::-1]