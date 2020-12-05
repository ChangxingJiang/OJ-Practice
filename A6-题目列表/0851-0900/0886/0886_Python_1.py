from typing import List


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        pass


if __name__ == "__main__":
    # True
    print(Solution().possibleBipartition(N=4, dislikes=[[1, 2], [1, 3], [2, 4]]))

    # False
    print(Solution().possibleBipartition(N=3, dislikes=[[1, 2], [1, 3], [2, 3]]))

    # False
    print(Solution().possibleBipartition(N=5, dislikes=[[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]))
