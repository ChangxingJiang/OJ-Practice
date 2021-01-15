from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = float("-inf")
        last1 = 0  # 绝对值最大的正数
        last2 = 0  # 绝对值最大的负数
        for num in nums:
            if num == 0:
                last1, last2 = 0, 0
                ans = max(ans, 0)
            elif num > 0:
                last1, last2 = ((last1 * num) if last1 != 0 else num), ((last2 * num) if last2 != 0 else 0)
                ans = max(ans, last1)
            else:
                last1, last2 = ((last2 * num) if last2 != 0 else 0), ((last1 * num) if last1 != 0 else num)
                ans = max(ans, last2, last1 if last1 != 0 else float("-inf"))

        return ans


if __name__ == "__main__":
    print(Solution().maxProduct([2, 3, -2, 4]))  # 6
    print(Solution().maxProduct([-2, 0, -1]))  # 0
    print(Solution().maxProduct([-2]))  # -2
    print(Solution().maxProduct([-4, -3, -2]))  # 12
