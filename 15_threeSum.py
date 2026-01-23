# 排序 + 双指针
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        for i in range(n):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return res

'''
and 的短路特性，当第一个条件不符合时，会直接跳出判断不进行 and 后面的条件判断。

# 写法1：合并在and中（原写法）
if i > 0 and nums[i] == nums[i - 1]:
    continue

# 写法2：拆分到if里（你说的更合理的写法）
if i > 0:
    if nums[i] == nums[i - 1]:
        continue
'''