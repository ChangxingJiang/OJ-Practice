from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        size = len(nums)

        dp = [0] * size
        for i in range(size):
            if dp[i] != 0:
                continue

            count = {}
            lst = []
            while i not in count and dp[i] == 0:
                count[i] = len(lst)
                lst.append(i)
                i = nums[i]

            # 遇到之前已经遍历的情况
            if dp[i] != 0:
                now = dp[i] + 1
                while lst:
                    dp[lst.pop()] = now
                    now += 1

            # 之前尚未遍历的情况，即进入循环的情况
            circle = len(lst) - count[i]  # 循环节长度
            for j in range(len(lst)):
                if j < count[i]:
                    dp[lst[j]] = len(lst) - j
                else:
                    dp[lst[j]] = circle

        return max(dp)


if __name__ == "__main__":
    print(Solution().arrayNesting([5, 4, 0, 3, 1, 6, 2]))  # 4
