#leetcode 20 有效的括号
'''
时间复杂度：O(n)
空间复杂度：O(n)
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '{':
                stack.append('}')
            elif c == '[':
                stack.append(']')
            elif not stack or stack[-1] != c:
                return False
            else:
                stack.pop()
            
        return not stack