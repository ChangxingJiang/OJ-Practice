from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        find = False
        for i in range(len(nums)):
            if nums[i - 1] > nums[i]:
                if not find:
                    find = True
                else:
                    return False
        return True


if __name__ == "__main__":
    print(Solution().check([3, 4, 5, 1, 2]))  # True
    print(Solution().check([2, 1, 3, 4]))  # False
    print(Solution().check([1, 2, 3]))  # True
    print(Solution().check([1, 1, 1]))  # True
    print(Solution().check([2, 1]))  # True
