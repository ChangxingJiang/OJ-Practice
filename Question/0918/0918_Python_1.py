from typing import List


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        ans1 = cur1 = 0
        for n in A:
            cur1 = n + max(cur1, 0)
            ans1 = max(ans1, cur1)

        if ans1 == 0:
            res = max(A)
            return res

        # 如果在循环数组中，一定包含首尾，那么用总和减去首尾最小值即可
        ans2 = cur2 = 0
        for n in A:
            cur2 = n + min(cur2, 0)
            ans2 = min(ans2, cur2)

        return max(ans1, sum(A) - ans2)


if __name__ == "__main__":
    print(Solution().maxSubarraySumCircular([1, -2, 3, -2]))  # 3
    print(Solution().maxSubarraySumCircular([5, -3, 5]))  # 10
    print(Solution().maxSubarraySumCircular([3, -1, 2, -1]))  # 4
    print(Solution().maxSubarraySumCircular([3, -2, 2, -3]))  # 3
    print(Solution().maxSubarraySumCircular([-2, -3, -1]))  # -1
