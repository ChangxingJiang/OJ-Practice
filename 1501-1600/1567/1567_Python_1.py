from typing import List


# 正反向分别查找
# O(N)

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        ans = 0

        # 正向查找
        now = 0
        temp = 1
        last = 0
        for num in nums:
            if num > 0:
                if temp > 0:
                    now += 1
                    last += 1
                    ans = max(ans, now)
                else:
                    last += 1
            elif num < 0:
                if temp > 0:
                    last += 1
                else:
                    last += 1
                    now = last
                    ans = max(ans, now)
                temp *= -1
            else:
                now = 0
                last = 0
                temp = 1

        # 反向查找
        now = 0
        temp = 1
        last = 0
        for num in nums[::-1]:
            if num > 0:
                if temp > 0:
                    now += 1
                    last += 1
                    ans = max(ans, now)
                else:
                    last += 1
            elif num < 0:
                if temp > 0:
                    last += 1
                else:
                    last += 1
                    now = last
                    ans = max(ans, now)
                temp *= -1
            else:
                now = 0
                last = 0
                temp = 1

        return ans


if __name__ == "__main__":
    print(Solution().getMaxLen(nums=[1, -2, -3, 4]))  # 4
    print(Solution().getMaxLen(nums=[0, 1, -2, -3, -4]))  # 3
    print(Solution().getMaxLen(nums=[-1, -2, -3, 0, 1]))  # 2
    print(Solution().getMaxLen(nums=[-1, 2]))  # 1
    print(Solution().getMaxLen(nums=[1, 2, 3, 5, -6, 4, 0, 10]))  # 4
