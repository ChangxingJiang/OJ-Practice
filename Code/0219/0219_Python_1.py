from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for i in range(len(nums)):
            n = nums[i]
            if n not in hashmap or i-hashmap[n]>k:
                hashmap[n] = i
            else:
                return True
        else:
            return False


if __name__ == "__main__":
    print(Solution().containsNearbyDuplicate([1, 2, 3, 1], 3))  # True
    print(Solution().containsNearbyDuplicate([1, 0, 1, 1], 1))  # True
    print(Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))  # False
    print(Solution().containsNearbyDuplicate([99, 99], 2))  # True
    print(Solution().containsNearbyDuplicate([1], 1))  # False
