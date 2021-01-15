from typing import List


class Solution:
    def minTime(self, time: List[int], m: int) -> int:
        n = len(time)

        # 完美变身“小杨刷题计划”的情况
        if n <= m:
            return 0

        left, right = 0, sum(time)
        while left < right:
            mid = (left + right) // 2

            # 检查当前mid是否符合要求
            day = 1
            today = 0
            helping = 0
            for n in time:
                today += n
                helping = max(helping, n)
                if today - helping > mid:
                    day += 1
                    today = n
                    helping = n

            if day > m:
                left = mid + 1
            else:
                right = mid

        return left


if __name__ == "__main__":
    print(Solution().minTime(time=[1, 2, 3, 3], m=2))  # 3
    print(Solution().minTime(time=[999, 999, 999], m=4))  # 0
