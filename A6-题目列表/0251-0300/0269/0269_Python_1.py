from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        pass


if __name__ == "__main__":
    # "wertf"
    print(Solution().alienOrder([
        "wrt",
        "wrf",
        "er",
        "ett",
        "rftt"
    ]))

    #  "zx"
    print(Solution().alienOrder([
        "z",
        "x"
    ]))

    # ""
    print(Solution().alienOrder([
        "z",
        "x",
        "z"
    ]))
