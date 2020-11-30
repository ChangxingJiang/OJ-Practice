from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major, count = -1, 0
        for n in nums:
            if count == 0:
                major = n
                count += 1
            elif major == n:
                count += 1
            else:
                count -= 1

        count = 0
        for n in nums:
            if major == n:
                count += 1

        return major if count > len(nums) // 2 else -1


if __name__ == "__main__":
    print(Solution().majorityElement([1, 2, 5, 9, 5, 9, 5, 5, 5]))  # 5
    print(Solution().majorityElement([3, 2]))  # -1
    print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))  # 2
    print(Solution().majorityElement([1, 2, 3]))  # -1
    print(Solution().majorityElement([3, 2, 3]))  # 3
    print(Solution().majorityElement([6, 5, 5]))  # 5

    print(Solution().majorityElement([3, 3, 4, 5, 3]))  # 3
