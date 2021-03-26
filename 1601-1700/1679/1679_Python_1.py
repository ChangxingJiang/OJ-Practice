import collections
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = collections.Counter([num for num in nums if num < k])

        ans = count[0] // 2

        for n1 in count:
            if n1 * 2 == k:
                ans += count[n1] // 2
            else:
                if k - n1 in count:
                    ans += min(count[n1], count[k - n1])
                    count[n1] = 0

        return ans


if __name__ == "__main__":
    print(Solution().maxOperations(nums=[1, 2, 3, 4], k=5))  # 2
    print(Solution().maxOperations(nums=[3, 1, 3, 4, 3], k=6))  # 1
