from typing import List


class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        min_val, max_val = A[0], A[-1]
        ans = max_val - min_val
        for i in range(len(A) - 1):
            a, b = A[i], A[i + 1]
            ans = min(ans, max(max_val - K, a + K) - min(min_val + K, b - K))
        return ans


if __name__ == "__main__":
    print(Solution().smallestRangeII([1], 0))  # 0
    print(Solution().smallestRangeII([0, 10], 2))  # 6
    print(Solution().smallestRangeII([1, 3, 6], 3))  # 3
    print(Solution().smallestRangeII([7, 8, 8], 5))  # 1
    print(Solution().smallestRangeII([3, 4, 7, 0], 5))  # 7
