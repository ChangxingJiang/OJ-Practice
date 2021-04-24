class Solution:
    def orchestraLayout(self, num: int, x: int, y: int) -> int:
        # 计算当前位置第几圈
        r = min(x, y, num - 1 - x, num - 1 - y)
        # print("当前圈数:", r)

        # 计算最外圈长度
        first = 4 * (num - 1)
        # print("最外圈长度:", first)

        # 计算所有外圈总长度
        outer = ((first + first - 8 * (r - 1)) * r) // 2
        # print("当前外圈总长度:", outer)

        # 计算当前圈长度
        x -= r
        y -= r
        num -= 2 * r

        if x == 0:  # 在上边
            inner = (y + 1)
        elif y == num - 1:  # 在右边
            inner = (num + x)
        elif x == num - 1:  # 在下边
            inner = (num + (num - 1) + (num - y - 1))
        else:  # 在左边
            inner = (num + (num - 1) + (num - 1) + (num - x - 1))
        # print("当前内圈总长度:", inner)

        ans = (inner + outer) % 9
        return ans if ans > 0 else 9


if __name__ == "__main__":
    print(Solution().orchestraLayout(3, 0, 2))  # 3
    print(Solution().orchestraLayout(4, 1, 2))  # 5

    # 自制用例
    print(Solution().orchestraLayout(1, 0, 0))  # 1
    print(Solution().orchestraLayout(2, 1, 0))  # 4
    print(Solution().orchestraLayout(5, 1, 2))  # 9
    print(Solution().orchestraLayout(5, 2, 2))  # 7
