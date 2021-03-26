from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minimum = min(nums)
        ans = 0
        for n in nums:
            ans += n - minimum
        return ans


if __name__ == "__main__":
    print(Solution().minMoves([1, 2, 3]))  # 3
    print(Solution().minMoves([1, 2, 5]))  # 5
    print(Solution().minMoves([1, 2147483647]))  # 2147483646
