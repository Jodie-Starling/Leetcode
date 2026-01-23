class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        stock = {}

        for char in magazine:
            stock[char] = stock.get(char, 0) + 1

        for char in ransomNote:
            if stock.get(char, 0) == 0:   # 判断要用双等号
                return False
            stock[char] -= 1

        return True