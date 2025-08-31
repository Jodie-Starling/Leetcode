# leetcode 349 两个数组的交集
# 版本一 使用字典和集合
'''
时间复杂度：O(n)
空间复杂度：O(n)
'''
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    # 使用哈希表存储一个数组中的所有元素
        table = {}
        for num in nums1:
            table[num] = table.get(num, 0) + 1
        
        # 使用集合存储结果
        res = set()
        for num in nums2:
            if num in table:
                res.add(num)
                del table[num]
        
        return list(res)
    


# 版本二 使用数组
'''
时间复杂度：O(n)
空间复杂度：O(n)
'''
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = [0]*1001
        count2 = [0]*1001
        result = []
        for i in range(len(nums1)):
            count1[nums1[i]]+=1
        for j in range(len(nums2)):
            count2[nums2[j]]+=1
        for k in range(1001):
            if count1[k]*count2[k]>0:   # 也可以 if count1[k] and count2[k]:
                result.append(k)
        return result



# 版本三 使用集合
'''
set 方法比数组容易，但占用空间比数组大，速度要比数组慢，set把数值映射到key上都要做hash计算。
时间复杂度：O(n)
空间复杂度：O(n)
'''
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))    # list()函数将集合转换为列表
    

list = []
list.append(1)
list.append(2)
list.append(3)
print(list)
list.pop()
print(list)