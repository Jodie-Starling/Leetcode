# 2026/1/17 242
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        record = [0] * 26

        for i in s:
            record[ord(i) - ord('a')] += 1

        for i in t:
            record[ord(i) - ord('a')] -= 1

        for i in record:
            if i != 0:
                return False

        return True