from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        now = 0
        ans = []
        for n in nums:
            now += n
            ans.append(now)
        return ans


if __name__ == "__main__":
    print(Solution().runningSum(nums=[1, 2, 3, 4]))  # [1,3,6,10]
    print(Solution().runningSum(nums=[1, 1, 1, 1, 1]))  # [1,2,3,4,5]
    print(Solution().runningSum(nums=[3, 1, 2, 10, 1]))  # [3,4,6,16,17]
