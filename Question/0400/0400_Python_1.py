class Solution:
    def findNthDigit(self, n: int) -> int:
        # 处理特殊情况
        if n == 0:
            return 0

        # 计算当前所处位数
        digit = 1
        while (val := 9 * digit * (10 ** (digit - 1))) < n:
            n -= val
            digit += 1

        # 计算当前所处数值
        n, bit = divmod(n - 1, digit)
        num = 10 ** (digit - 1) + n

        # 计算最终结果
        return int(str(num)[bit])


if __name__ == "__main__":
    print(Solution().findNthDigit(3))  # 3
    print(Solution().findNthDigit(11))  # 0
