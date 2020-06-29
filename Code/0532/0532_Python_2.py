from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k <0:
            return 0

        ans = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] - nums[j] == k:
                    ans.add((nums[i], nums[j]))
                elif nums[j] - nums[i] == k:
                    ans.add((nums[j], nums[i]))
        return len(ans)


if __name__ == "__main__":
    print(Solution().findPairs([3, 1, 4, 1, 5], 2))  # 2
    print(Solution().findPairs([1, 2, 3, 4, 5], 1))  # 4
    print(Solution().findPairs([1, 3, 1, 5, 4], 0))  # 1
