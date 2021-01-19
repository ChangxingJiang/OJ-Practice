from typing import List


class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        d1 = abs(target[0]) + abs(target[1])
        for ghost in ghosts:
            d2 = abs(target[1] - ghost[1]) +abs (target[0] - ghost[0])
            if d2 <= d1:
                return False
        return True


if __name__ == "__main__":
    # True
    print(Solution().escapeGhosts(ghosts=[[1, 0], [0, 3]], target=[0, 1]))

    # False
    print(Solution().escapeGhosts(ghosts=[[1, 0]], target=[2, 0]))

    # False
    print(Solution().escapeGhosts(ghosts=[[2, 0]], target=[1, 0]))

    # False
    print(Solution().escapeGhosts(ghosts=[[5, 0], [-10, -2], [0, -5], [-2, -2], [-7, 1]], target=[7, 7]))

    # True
    print(Solution().escapeGhosts(ghosts=[[-1, 0], [0, 1], [-1, 0], [0, 1], [-1, 0]], target=[0, 0]))
