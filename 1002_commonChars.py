#2026/1/17 1002
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        min_freq = [0] * 26
        for i in words[0]:
            min_freq[ord(i) - ord('a')] += 1

        for word in words[1:]:
            char_freq = [0] * 26
            for i in word:
                char_freq[ord(i) - ord('a')] += 1
            for i in range(26):
                min_freq[i] = min(min_freq[i], char_freq[i])

        res = []

        for i in range(26):
            while min_freq[i] > 0:
                res.append(chr(ord('a')+i))
                # Python 里把数字转字符的函数是 chr()，不是 char()
                # 你要还原的是第 i 个字母（比如 i=1 是 'b'），而不是用它的数量 min_freq[i] 去算
                min_freq[i] -= 1

        return res