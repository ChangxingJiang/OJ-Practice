from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        pass


if __name__ == "__main__":
    # ["eat","oath"]
    print(Solution().findWords(
        board=[["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
        words=["oath", "pea", "eat", "rain"]))

    # []
    print(Solution().findWords(board=[["a", "b"], ["c", "d"]], words=["abcb"]))
