class Solution:
    def totalMoney(self, n: int) -> int:
        week, surplus = divmod(n, 7)

        # 计算整周的结果
        n1 = 21 * week + 7 * (1 + week) * week // 2

        # 计算最后一周的结果
        n2 = (week + 1 + week + surplus) * surplus // 2

        return n1 + n2


if __name__ == "__main__":
    print(Solution().totalMoney(4))  # 10
    print(Solution().totalMoney(10))  # 37
    print(Solution().totalMoney(20))  # 96
