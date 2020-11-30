from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        pass


if __name__ == "__main__":
    # True
    print(Solution().containsNearbyAlmostDuplicate(nums=[1, 2, 3, 1], k=3, t=0))

    # True
    print(Solution().containsNearbyAlmostDuplicate(nums=[1, 0, 1, 1], k=1, t=2))

    # False
    print(Solution().containsNearbyAlmostDuplicate(nums=[1, 5, 9, 1, 5, 9], k=2, t=3))
