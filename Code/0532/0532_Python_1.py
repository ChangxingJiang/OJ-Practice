from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if len(nums) < 2:
            return 0

        nums.sort()

        idx1 = 0
        idx2 = 1
        ans = set()
        while idx1 < len(nums) - 1 and idx2 <= len(nums) - 1:
            if idx1 == idx2:
                idx2 += 1
            s = nums[idx2] - nums[idx1]
            if s > k:
                idx1 += 1
            elif s < k:
                idx2 += 1
            else:
                ans.add((nums[idx1], nums[idx2]))
                idx1 += 1

        return len(ans)


if __name__ == "__main__":
    print(Solution().findPairs([3, 1, 4, 1, 5], 2))  # 2
    print(Solution().findPairs([1, 2, 3, 4, 5], 1))  # 4
    print(Solution().findPairs([1, 3, 1, 5, 4], 0))  # 1
