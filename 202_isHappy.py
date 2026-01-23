class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = (sum(int(i) ** 2 for i in str(n)))   # 极简流，各个数位上数字的平方和

        return True

# 上面逻辑简单，效率高，但str(n)会占用新内存空间。下面是数学设计的函数实现各个数位平方和
def get_sum():
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit ** 2
        n = n // 10
    return sum