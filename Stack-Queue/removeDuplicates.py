#leetcode 1047 删除字符串中的所有相邻重复项
'''
时间复杂度：O(n)
空间复杂度：O(n)
'''
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)   #'分隔符'.join(可迭代的字符串) 返回字符串 （可迭代的字符串中元素必须是字符串，数字1不属于字符串）