#leetcode 142 环形链表
#（版本一）快慢指针法
'''
假设头节点到环入口的距离为 a，环入口到相遇点的距离为 b，环的长度为 r。
a + b = n * r 其中 n 为正整数
所以a = n * r - b,即：都一次一格走，慢指针从头开始，快指针在环内接着绕圈，最后相遇时必然在环的入口。
时间复杂度：O(n)
空间复杂度：O(1)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # If there is a cycle, the slow and fast pointers will eventually meet
            if slow == fast:
                # Move one of the pointers back to the start of the list
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        # If there is no cycle, return None
        return None
    


#（版本二）集合法
'''
时间复杂度：O(n)
空间复杂度：O(n)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        visited = set()
        
        while head:
            if head in visited:
                return head
            visited.add(head)
            head = head.next
        
        return None