from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        last = None
        num = 0
        for n in nums:
            if n == last:
                num += 1
            elif num > 0:
                num -= 1
            else:
                last = n
                num = 0
        return last


if __name__ == "__main__":
    print(Solution().majorityElement([1, 2, 3, 2, 2, 2, 5, 4, 2]))  # 2
