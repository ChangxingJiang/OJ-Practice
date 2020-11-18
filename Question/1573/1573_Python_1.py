# 数学
# O(N)

class Solution:
    def numWays(self, s: str) -> int:
        num = s.count("1")

        # 处理无法有效拆分3的情况
        if num % 3 != 0:
            return 0

        # 处理没有1的情况
        if num == 0:
            if len(s) < 3:
                return 0
            else:
                return ((len(s) - 1) * (len(s) - 2) // 2) % (10 ** 9 + 7)

        # 计算每个子字符串的1的数量
        num //= 3

        # 统计每组3之间的0的数量
        num1, num2 = 0, 0
        now = 0
        for ch in s:
            if ch == "1":
                now += 1
            else:
                if now == num:
                    num1 += 1
                if now == num * 2:
                    num2 += 1

        return ((num1 + 1) * (num2 + 1)) % (10 ** 9 + 7)


if __name__ == "__main__":
    print(Solution().numWays(s="10101"))  # 4
    print(Solution().numWays(s="1001"))  # 0
    print(Solution().numWays(s="0000"))  # 3
    print(Solution().numWays(s="100100010100110"))  # 12
    print(Solution().numWays(s="00000000"))  # 21
