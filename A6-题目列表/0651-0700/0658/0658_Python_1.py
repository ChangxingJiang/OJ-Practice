from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pass


if __name__ == "__main__":
    print(Solution().findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=3))  # [1,2,3,4]
    print(Solution().findClosestElements(arr = [1,2,3,4,5], k = 4, x = -1))  # [1,2,3,4]
