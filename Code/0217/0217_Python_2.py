from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n not in hashset:
                hashset.add(n)
            else:
                return True
        else:
            return False


if __name__ == "__main__":
    print(Solution().containsDuplicate([1, 2, 3, 1]))  # True
    print(Solution().containsDuplicate([1, 2, 3, 4]))  # False
    print(Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # True
