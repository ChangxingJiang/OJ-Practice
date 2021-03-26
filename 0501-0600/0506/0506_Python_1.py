from typing import List


class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        order = sorted(nums, reverse=True)
        ans = []
        for n in nums:
            idx = order.index(n)
            if idx == 0:
                ans.append("Gold Medal")
            elif idx == 1:
                ans.append("Silver Medal")
            elif idx == 2:
                ans.append("Bronze Medal")
            else:
                ans.append(str(idx + 1))
        return ans


if __name__ == "__main__":
    print(Solution().findRelativeRanks([5, 4, 3, 2, 1]))  # ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
