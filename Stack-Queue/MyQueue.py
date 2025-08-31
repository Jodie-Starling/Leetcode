#leetcode 232 用栈实现队列
#栈是先进后出（LIFO）的数据结构，记住数据流方向。
'''
用栈来实现队列
时间复杂度：O(1) amortized for push, O(n) for pop and peek
空间复杂度：O(n)
'''
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack1 and not self.stack2:
            return None
        if self.stack2:
            return self.stack2.pop()
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack1 and not self.stack2:
            return None
        if self.stack2:
            temp = self.stack2.pop()
            self.stack2.append(temp)
            return temp
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            temp = self.stack2.pop()
            self.stack2.append(temp)
            return temp

    def empty(self) -> bool:
        if not self.stack1 and not self.stack2:
            return True
        else:
            return False



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()