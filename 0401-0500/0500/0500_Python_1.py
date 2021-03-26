from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard = {
            "Q": 0, "W": 0, "E": 0, "R": 0, "T": 0, "Y": 0, "U": 0, "I": 0, "O": 0, "P": 0,
            "A": 1, "S": 1, "D": 1, "F": 1, "G": 1, "H": 1, "J": 1, "K": 1, "L": 1,
            "Z": 2, "X": 2, "C": 2, "V": 2, "B": 2, "N": 2, "M": 2
        }

        def helper(word):
            return len(set([keyboard[s] for s in word.upper()])) == 1

        return [word for word in words if helper(word)]


if __name__ == "__main__":
    print(Solution().findWords(["Hello", "Alaska", "Dad", "Peace"]))  # ["Alaska", "Dad"]
