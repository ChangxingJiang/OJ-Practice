from typing import List


class Solution:
    def bonus(self, n: int, leadership: List[List[int]], operations: List[List[int]]) -> List[int]:
        pass


if __name__ == "__main__":
    print(Solution().bonus(n=6,
                           leadership=[[1, 2], [1, 6], [2, 3], [2, 5], [1, 4]],
                           operations=[[1, 1, 500], [2, 2, 50], [3, 1], [2, 6, 15], [3, 1]]
                           ))  # [650, 665]
