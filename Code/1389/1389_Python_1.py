from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(nums)):
            target.insert(index[i], nums[i])
        return target


if __name__ == "__main__":
    print(Solution().createTargetArray(nums=[0, 1, 2, 3, 4], index=[0, 1, 2, 2, 1]))  # [0,4,1,3,2]
    print(Solution().createTargetArray(nums=[1, 2, 3, 4, 0], index=[0, 1, 2, 3, 0]))  # [0,1,2,3,4]
    print(Solution().createTargetArray(nums=[1], index=[0]))  # [1]
