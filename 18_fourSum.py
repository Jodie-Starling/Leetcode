# 四数之和 两层遍历+双指针
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        for k in range(n - 3):   # 控制好边界
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            if nums[k] > target and target > 0:
                break

            for i in range(k + 1, n - 2):
                if i > k + 1 and nums[i] == nums[i - 1]:
                    continue
                if nums[k] + nums[i] > target and target > 0:
                    break

                left = i + 1
                right = n - 1

                while left < right:
                    sum = nums[k] +nums[i] + nums[left] + nums[right]
                    if sum < target:
                        left += 1
                    elif sum > target:
                        right -= 1
                    else:
                        res.append([nums[k], nums[i], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
        return res