from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = set()
        for n in nums:
            if target - n in lst:
                return [n, target - n]
            else:
                lst.add(n)


if __name__ == "__main__":
    # [2,7] 或者 [7,2]
    print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))

    # [10,30] 或者 [30,10]
    print(Solution().twoSum(nums=[10, 26, 30, 31, 47, 60], target=40))
