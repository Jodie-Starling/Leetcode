# 螺旋矩阵 模拟过程

'''
右→左，下→上 要控制条件是否成立
防止重复填充
'''

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return []

        matrix = [[0] * n for _ in range(n)]
        left, right = 0, n - 1
        top, bottom = 0, n - 1
        num = 1  # 从 1 开始！

        while num <= n * n:
            # 1. 上边：左 → 右
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            top += 1

            # 2. 右边：上 → 下
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
            right -= 1

            # 3. 下边：右 → 左（只有剩余多行时才填）
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    matrix[bottom][col] = num
                    num += 1
                bottom -= 1

            # 4. 左边：下 → 上（只有剩余多列时才填）
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    matrix[row][left] = num
                    num += 1
                left += 1

        return matrix