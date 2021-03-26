from typing import List


class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        pass


if __name__ == "__main__":
    # 0.16666666666666666
    print(Solution().frogPosition(n=7, edges=[[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], t=2, target=4))

    # 0.3333333333333333
    print(Solution().frogPosition(n=7, edges=[[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], t=1, target=7))

    # 0.16666666666666666
    print(Solution().frogPosition(n=7, edges=[[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], t=20, target=6))
