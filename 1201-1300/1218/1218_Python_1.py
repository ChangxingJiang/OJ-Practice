import collections
from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        ans = 0
        count = collections.Counter()

        for n in arr:
            if n - difference in count:
                count[n] = count[n - difference] + 1
            else:
                count[n] = 1
            ans = max(ans, count[n])
        return ans


if __name__ == "__main__":
    print(Solution().longestSubsequence(arr=[1, 2, 3, 4], difference=1))  # 4
    print(Solution().longestSubsequence(arr=[1, 3, 5, 7], difference=1))  # 1
    print(Solution().longestSubsequence(arr=[1, 5, 7, 8, 5, 3, 4, 2, 1], difference=-2))  # 4
    print(Solution().longestSubsequence(arr=[3, 0, -3, 4, -4, 7, 6], difference=3))  # 2
