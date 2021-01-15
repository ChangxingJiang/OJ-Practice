from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        for i1 in range(len(nums)):
            n1 = nums[i1]
            for i2 in range(i1 + 1, min(i1 + k + 1, len(nums))):
                n2 = nums[i2]
                if abs(n2 - n1) <= t:
                    return True
        return False


if __name__ == "__main__":
    # True
    print(Solution().containsNearbyAlmostDuplicate(nums=[1, 2, 3, 1], k=3, t=0))

    # True
    print(Solution().containsNearbyAlmostDuplicate(nums=[1, 0, 1, 1], k=1, t=2))

    # False
    print(Solution().containsNearbyAlmostDuplicate(nums=[1, 5, 9, 1, 5, 9], k=2, t=3))
