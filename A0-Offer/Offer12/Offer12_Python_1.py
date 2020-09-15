from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        pass


if __name__ == "__main__":
    # True
    print(Solution().exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED"))

    # False
    print(Solution().exist(board=[["a", "b"], ["c", "d"]], word="abcd"))
