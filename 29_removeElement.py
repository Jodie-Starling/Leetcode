# 2025/12/26二刷

'''
双指针法用 O(n) 时间甚至 O(1) 额外空间解决问题，大幅提升效率，
避免暴力 O(n²) 的嵌套循环。
'''

'''
慢指针 slow：指向“新数组”（移除后有效部分）的当前待填充位置。
快指针 fast：负责遍历整个数组，寻找不等于 val 的元素。
'''


# 同向双指针
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1

        return slow


# 相向双指针 在某些情况下甚至比快慢指针更高效（平均交换次数更少）
class Solution:
         def removeElement(self, nums: List[int], val: int) -> int:
            slow = 0
            fast = len(nums) - 1
            while slow <= fast:
                if nums[slow] != val:
                    slow += 1
                else:
                    nums[slow] = nums[fast]
                    fast -= 1

            return slow