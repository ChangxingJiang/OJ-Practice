from typing import List


class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        n = len(x)
        count = {}
        for i in range(n):
            xx = x[i]
            yy = y[i]
            if xx not in count:
                count[xx] = yy
            else:
                count[xx] = max(count[xx], yy)
        nums = sorted(count.values(), reverse=True)
        if len(nums) < 3:
            return -1
        return sum(nums[:3])


if __name__ == "__main__":
    print(Solution().maxSumDistinctTriplet(x=[1, 2, 1, 3, 2], y=[5, 3, 4, 6, 2]))  # 14
    print(Solution().maxSumDistinctTriplet(x=[1, 2, 1, 2], y=[4, 5, 6, 7]))  # -1
