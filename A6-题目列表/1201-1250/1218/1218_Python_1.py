from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        pass


if __name__ == "__main__":
    print(Solution().longestSubsequence(arr=[1, 2, 3, 4], difference=1))  # 4
    print(Solution().longestSubsequence(arr=[1, 3, 5, 7], difference=1))  # 1
    print(Solution().longestSubsequence(arr=[1, 5, 7, 8, 5, 3, 4, 2, 1], difference=-2))  # 4
