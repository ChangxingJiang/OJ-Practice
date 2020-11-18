from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        last = 0
        for n in nums:
            last += n
            ans.append(last)
        return ans


if __name__ == "__main__":
    print(Solution().runningSum(nums=[1, 2, 3, 4]))  # [1,3,6,10]
    print(Solution().runningSum(nums=[1,1,1,1,1]))  # [1,2,3,4,5]
    print(Solution().runningSum(nums=[3,1,2,10,1]))  # [3,4,6,16,17]
