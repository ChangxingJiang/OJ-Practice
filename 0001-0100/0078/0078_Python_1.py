from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(2 ** len(nums)):
            now = []
            idx = len(nums) - 1
            while i:
                if i & 1:
                    now.append(nums[idx])
                idx -= 1
                i >>= 1
            ans.append(now)

        return ans


if __name__ == "__main__":
    # [
    #   [3],
    #   [1],
    #   [2],
    #   [1,2,3],
    #   [1,3],
    #   [2,3],
    #   [1,2],
    #   []
    # ]
    print(Solution().subsets(nums=[1, 2, 3]))
