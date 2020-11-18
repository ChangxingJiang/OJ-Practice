import bisect
from typing import List


# 数组、二分查找
# O(NlogN)


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()

        ans = 0

        for i in range(len(nums)):
            val = nums[i]
            idx = bisect.bisect_right(nums, target - val)

            if idx > i:
                ans += 2 ** (idx - i - 1)

            # print(i, "->", idx, "(", target - val, ")")

        return ans % (10 ** 9 + 7)


if __name__ == "__main__":
    print(Solution().numSubseq(nums=[3, 5, 6, 7], target=9))  # 4
    print(Solution().numSubseq(nums=[3, 3, 6, 8], target=10))  # 6
    print(Solution().numSubseq(nums=[2, 3, 3, 4, 6, 7], target=12))  # 61
    print(Solution().numSubseq(nums=[5, 2, 4, 1, 7, 6, 8], target=16))  # 127
