from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n1 = n2 = float("inf")
        for num in nums:
            if num < n1:
                n1 = num
            elif n1 < num < n2:
                n2 = num
            elif n2 < num:
                return True
        return False


if __name__ == "__main__":
    print(Solution().increasingTriplet([1, 2, 3, 4, 5]))  # True
    print(Solution().increasingTriplet([5, 4, 3, 2, 1]))  # False
    print(Solution().increasingTriplet([2, 1, 5, 0, 4, 6]))  # True
    print(Solution().increasingTriplet([1, 1, -2, 6]))  # False
