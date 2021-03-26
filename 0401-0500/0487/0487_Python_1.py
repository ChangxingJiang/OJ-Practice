from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 1
        last = -1
        now = 0
        for n in nums:
            if n == 1:
                now += 1
                ans = max(ans, last + now + 1)
            else:
                last = now
                now = 0
                ans = max(ans, last + 1)

        return ans


if __name__ == "__main__":
    print(Solution().findMaxConsecutiveOnes([1, 0, 1, 1, 0]))  # 4
    print(Solution().findMaxConsecutiveOnes([1]))  # 1
    print(Solution().findMaxConsecutiveOnes([1, 0]))  # 2
