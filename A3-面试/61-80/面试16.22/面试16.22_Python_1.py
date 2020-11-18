from typing import List


class Solution:
    def printKMoves(self, K: int) -> List[str]:
        pass


if __name__ == "__main__":
    # ["R"]
    print(Solution().printKMoves(0))

    # [
    #   "_X",
    #   "LX"
    # ]
    print(Solution().printKMoves(2))

    # [
    #   "_U",
    #   "X_",
    #   "XX"
    # ]
    print(Solution().printKMoves(5))
