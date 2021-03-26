import collections
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        count = collections.defaultdict(set)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i:
                    count[nums[i] + nums[j]].add((i, j))

        ans = set()
        for k in range(len(nums)):
            if -nums[k] in count:
                for i, j in count[-nums[k]]:
                    if i != k and j != k:
                        ans.add(tuple(sorted([nums[i], nums[j], nums[k]])))

        return [list(res) for res in ans]


if __name__ == "__main__":
    # [
    #   [-1, 0, 1],
    #   [-1, -1, 2]
    # ]
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))

    # []
    print(Solution().threeSum([]))

    # []
    print(Solution().threeSum([0]))
