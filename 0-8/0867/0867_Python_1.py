from typing import List


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        pass


if __name__ == "__main__":
    # [[1,4,7],[2,5,8],[3,6,9]]
    print(Solution().transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    # [[1,4],[2,5],[3,6]]
    print(Solution().transpose([[1, 2, 3], [4, 5, 6]]))
