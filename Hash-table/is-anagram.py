#leetcode 242
#哈希表
'''
时间复杂度：O(n)
空间复杂度：O(1)
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0] * 26
        for i in s:
            #并不需要记住字符a的ASCII，只要求出一个相对数值就可以了
            record[ord(i) - ord("a")] += 1
        for i in t:
            record[ord(i) - ord("a")] -= 1
        for i in range(26):
            if record[i] != 0:
                #record数组如果有的元素不为零0，说明字符串s和t 一定是谁多了字符或者谁少了字符。
                return False
        return True
    

    
#defaultdict解法
'''
defaultdict 的主要特点是当访问一个不存在的键时，它会自动创建该键并为其分配一个默认值，而不是抛出 KeyError 异常。
时间复杂度：O(n)
空间复杂度：O(1)
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for x in s:
            s_dict[x] += 1
        
        for x in t:
            t_dict[x] += 1
        return s_dict == t_dict
    


#Counter解法
'''

时间复杂度：O(n)
空间复杂度：O(1)
'''
class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        a_count = Counter(s)        # 统计字符串 s 中每个字符的出现次数；Counter({'l': 1, 'i': 1, 's': 1, 't': 1, 'e': 1, 'n': 1})
        b_count = Counter(t)        # 统计字符串 t 中每个字符的出现次数；Counter({'l': 1, 'i': 1, 's': 1, 't': 1, 'e': 1, 'n': 1})
        return a_count == b_count