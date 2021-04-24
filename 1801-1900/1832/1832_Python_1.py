import collections


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(collections.Counter(sentence)) == 26


if __name__ == "__main__":
    print(Solution().checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))  # True
    print(Solution().checkIfPangram("leetcode"))  # True
