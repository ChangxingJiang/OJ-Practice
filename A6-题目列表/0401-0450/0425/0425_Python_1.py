from typing import List


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        pass


if __name__ == "__main__":
    # [
    #   [ "wall",
    #     "area",
    #     "lead",
    #     "lady"
    #   ],
    #   [ "ball",
    #     "area",
    #     "lead",
    #     "lady"
    #   ]
    # ]
    print(Solution().wordSquares(["area", "lead", "wall", "lady", "ball"]))

    # [
    #   [ "baba",
    #     "abat",
    #     "baba",
    #     "atan"
    #   ],
    #   [ "baba",
    #     "abat",
    #     "baba",
    #     "atal"
    #   ]
    # ]
    print(Solution().wordSquares(["abat", "baba", "atan", "atal"]))
