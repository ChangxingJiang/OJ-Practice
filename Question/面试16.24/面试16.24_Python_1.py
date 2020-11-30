import collections
from typing import List


class Solution:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        count = collections.Counter()
        for num in nums:
            another = target - num
            if count[another] > 0:
                count[another] -= 1
                ans.append([another, num])
            else:
                count[num] += 1

        return ans


if __name__ == "__main__":
    # [[5,6]]
    print(Solution().pairSums(nums=[5, 6, 5], target=11))

    # [[5,6],[5,6]]
    print(Solution().pairSums(nums=[5, 6, 5, 6], target=11))
