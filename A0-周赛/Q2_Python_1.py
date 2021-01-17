import collections
from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        count = collections.defaultdict(list)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                count[nums[i] * nums[j]].append((i, j))

        ans = 0
        for lst in count.values():
            for i in range(len(lst)):
                for j in range(i + 1, len(lst)):
                    if lst[i][0] != lst[i][1] != lst[j][0] != lst[j][1]:
                        ans += 8

        return ans


if __name__ == "__main__":
    print(Solution().tupleSameProduct([2, 3, 4, 6]))  # 8
    print(Solution().tupleSameProduct([1, 2, 4, 5, 10]))  # 16
    print(Solution().tupleSameProduct([2, 3, 4, 6, 8, 12]))  # 40
    print(Solution().tupleSameProduct([2, 3, 5, 7]))  # 0
