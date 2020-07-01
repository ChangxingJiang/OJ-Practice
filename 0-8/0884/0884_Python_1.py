from typing import List


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        pass


if __name__ == "__main__":
    print(Solution().uncommonFromSentences(A="this apple is sweet", B="this apple is sour"))  # ["sweet","sour"]
    print(Solution().uncommonFromSentences(A="apple apple", B="banana"))  # ["banana"]
