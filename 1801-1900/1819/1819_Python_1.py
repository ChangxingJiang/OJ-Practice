import math
from typing import List


class Solution:
    _MAXIMUM = 2 * (10 ** 5)

    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        nums = set(nums)
        m = max(nums)

        ans = 0

        for i in range(1, m + 1):
            if i in nums:
                ans += 1
                continue
                
            gcd = 0
            for j in range(i, m + 1, i):
                if j in nums:
                    if not gcd:
                        gcd = j
                    else:
                        gcd = math.gcd(gcd, j)
                    if gcd == i:
                        ans += 1
                        break

        return ans


if __name__ == "__main__":
    print(Solution().countDifferentSubsequenceGCDs(nums=[6, 10, 3]))  # 5
    print(Solution().countDifferentSubsequenceGCDs(nums=[5, 15, 40, 5, 6]))  # 7
