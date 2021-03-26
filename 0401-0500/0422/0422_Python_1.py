from typing import List


class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i in range(len(words)):
            for j in range(len(words[i])):
                if len(words) <= j or len(words[j]) <= i or words[i][j] != words[j][i]:
                    return False
        return True


if __name__ == "__main__":
    # True
    print(Solution().validWordSquare([
        "abcd",
        "bnrt",
        "crmy",
        "dtye"
    ]))

    # True
    print(Solution().validWordSquare([
        "abcd",
        "bnrt",
        "crm",
        "dt"
    ]))

    # False
    print(Solution().validWordSquare([
        "ball",
        "area",
        "read",
        "lady"
    ]))

    # False
    print(Solution().validWordSquare([
        "abc",
        "b"
    ]))
