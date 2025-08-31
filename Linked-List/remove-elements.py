#（版本一）虚拟头节点法
'''
时间复杂度O(n)
空间复杂度O(1)
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 创建虚拟头部节点以简化删除过程
        dummy_head = ListNode(next = head)
        
        # 遍历列表并删除值为val的节点
        current = dummy_head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        
        return dummy_head.next  #返回的是新链表的头指针
    

#（版本二）直接删除法
'''
时间复杂度O(n)
空间复杂度O(1)
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 第一步：处理头节点 - 可能有连续多个头节点需要删除
        while head and head.val == val:
            head = head.next
        
        # 第二步：处理后续节点
        current = head  # current指向当前检查节点的前一个节点
        
        while current and current.next:
            if current.next.val == val:
                # 删除current.next节点
                current.next = current.next.next
            else:
                # 移动到下一个节点
                current = current.next
        
        return head


'''
移除链表元素：
直接使用原来的链表来进行删除操作，就需要把头部单拎出来先处理；
设置一个虚拟头结点在进行删除操作；
时间复杂度O(n)
空间复杂度O(1)
ListNode类往往刷题时力扣就已经写好了，直接使用即可。但是自己的完整程序是需要自己写的。面试时问面试官需不需要写。
'''