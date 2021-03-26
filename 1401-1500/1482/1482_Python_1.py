from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        size = len(bloomDay)

        # 处理花圃中的花不够用的情况
        if m * k > size:
            return -1

        # 二分查找寻找目标天数
        left, right = 1, max(bloomDay)
        while left < right:
            mid = (left + right) // 2

            need = m
            now = 0
            i = 0
            while need > 0 and i < size:
                if bloomDay[i] <= mid:
                    now += 1
                    if now == k:
                        now = 0
                        need -= 1
                else:
                    now = 0
                i += 1

            if need > 0:
                left = mid + 1
            else:
                right = mid

        return right


if __name__ == "__main__":
    print(Solution().minDays(bloomDay=[1, 10, 3, 10, 2], m=3, k=1))  # 3
    print(Solution().minDays(bloomDay=[1, 10, 3, 10, 2], m=3, k=2))  # -1
    print(Solution().minDays(bloomDay=[7, 7, 7, 7, 12, 7, 7], m=2, k=3))  # 12
    print(Solution().minDays(bloomDay=[1000000000, 1000000000], m=1, k=1))  # 1000000000
    print(Solution().minDays(bloomDay=[1, 10, 2, 9, 3, 8, 4, 7, 5, 6], m=4, k=2))  # 9
