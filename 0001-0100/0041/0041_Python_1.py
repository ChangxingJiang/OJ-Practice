from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        size = len(nums)
        for i1 in range(size):
            n1 = i1 + 1
            while nums[i1] != n1:
                i2 = nums[i1] - 1
                if 0 <= i2 < size:
                    if nums[i1] != nums[i2]:
                        nums[i1], nums[i2] = nums[i2], nums[i1]
                    else:
                        nums[i2] = -1
                else:
                    nums[i1] = -1
                    break

        for i in range(size):
            if nums[i] == -1:
                return i + 1

        return size + 1


if __name__ == "__main__":
    print(Solution().firstMissingPositive([1, 2, 0]))  # 3
    print(Solution().firstMissingPositive([3, 4, -1, 1]))  # 2
    print(Solution().firstMissingPositive([7, 8, 9, 11, 12]))  # 1
    print(Solution().firstMissingPositive([]))  # 1
    print(Solution().firstMissingPositive([1, 1]))  # 2
