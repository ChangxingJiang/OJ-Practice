from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            bit = True
            while n > 0:
                n = n // 10
                bit = not bit
            ans += bit
        return ans


if __name__ == "__main__":
    print(Solution().findNumbers([12, 345, 2, 6, 7896]))  # 2
    print(Solution().findNumbers([555, 901, 482, 1771]))  # 1
