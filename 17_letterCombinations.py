class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone_map = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

        res = []
        path = []

        def backtracking(index):
            if index == len(digits):   # 递归先写回退条件
                res.append(''.join(path))
                return

            digit = digits[index]
            letters = phone_map[digit]

            for char in letters:
                path.append(char)
                backtracking(index + 1)
                path.pop()

        backtracking(0)
        return res