from typing import List


class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        pass


if __name__ == "__main__":
    # 7
    print(Solution().kthSmallest(mat=[[1, 3, 11], [2, 4, 6]], k=5))

    # 17
    print(Solution().kthSmallest(mat=[[1, 3, 11], [2, 4, 6]], k=9))

    # 9
    print(Solution().kthSmallest(mat=[[1, 10, 10], [1, 4, 5], [2, 3, 6]], k=7))

    # 12
    print(Solution().kthSmallest(mat=[[1, 1, 10], [2, 2, 9]], k=7))
