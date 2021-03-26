from typing import List


class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        pass


if __name__ == "__main__":
    # [60,68]
    print(Solution().minAvailableDuration(slots1=[[10, 50], [60, 120], [140, 210]], slots2=[[0, 15], [60, 70]],
                                          duration=8))

    # []
    print(Solution().minAvailableDuration(slots1=[[10, 50], [60, 120], [140, 210]], slots2=[[0, 15], [60, 70]],
                                          duration=12))
