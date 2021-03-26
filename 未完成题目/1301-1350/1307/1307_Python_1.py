from typing import List


class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().isSolvable(words=["SEND", "MORE"], result="MONEY"))  # True
    print(Solution().isSolvable(words=["SIX", "SEVEN", "SEVEN"], result="TWENTY"))  # True
    print(Solution().isSolvable(words=["THIS", "IS", "TOO"], result="FUNNY"))  # True
    print(Solution().isSolvable(words=["LEET", "CODE"], result="POINT"))  # False
