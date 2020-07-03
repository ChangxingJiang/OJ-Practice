from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        pass


if __name__ == "__main__":
    print(Solution().minimumAbsDifference(arr=[4, 2, 1, 3]))  # [[1,2],[2,3],[3,4]]
    print(Solution().minimumAbsDifference(arr=[1, 3, 6, 10, 15]))  # [[1,3]]
    print(Solution().minimumAbsDifference(arr=[3, 8, -10, 23, 19, -4, -14, 27]))  # [[-14,-10],[19,23],[23,27]]
