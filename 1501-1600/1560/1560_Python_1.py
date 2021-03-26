from typing import List


class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        circle = [i for i in range(1, n + 1)]
        start, end = rounds[0], rounds[-1]

        if start <= end:
            return circle[start - 1:end]
        else:
            return circle[:end] + circle[start - 1:]


if __name__ == "__main__":
    print(Solution().mostVisited(n=4, rounds=[1, 3, 1, 2]))  # [1,2]
    print(Solution().mostVisited(n=2, rounds=[2, 1, 2, 1, 2, 1, 2, 1, 2]))  # [2]
    print(Solution().mostVisited(n=7, rounds=[1, 3, 5, 7]))  # [1,2,3,4,5,6,7]
