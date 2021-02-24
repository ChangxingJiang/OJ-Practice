class Solution:
    def minimumBoxes(self, n: int) -> int:
        # ---------- 二分计算可以堆放的最大层数 ----------
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if mid * (mid + 1) * (mid + 2) // 6 < n:
                left = mid + 1
            else:
                right = mid
        left -= 1

        cell = left * (left + 1) * (left + 2) // 6

        # 计算当前占地面积（即最下层的盒子数量）
        area = (1 + left) * left // 2

        # ---------- 二分计算还需要继续放置的砖块 ----------
        target = n - cell
        left, right = 0, target
        while left < right:
            mid = (left + right) // 2
            if mid * (mid + 1) // 2 < target:
                left = mid + 1
            else:
                right = mid

        return area + left


if __name__ == "__main__":
    print(Solution().minimumBoxes(1))  # 1
    print(Solution().minimumBoxes(3))  # 3
    print(Solution().minimumBoxes(4))  # 3
    print(Solution().minimumBoxes(5))  # 4
    print(Solution().minimumBoxes(6))  # 5
    print(Solution().minimumBoxes(7))  # 5
    print(Solution().minimumBoxes(10))  # 6

    print(Solution().minimumBoxes(11))  # 7
    print(Solution().minimumBoxes(12))  # 8
    print(Solution().minimumBoxes(13))  # 8
    print(Solution().minimumBoxes(14))  # 9
    print(Solution().minimumBoxes(15))  # 9
