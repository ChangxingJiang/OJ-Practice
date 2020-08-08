from typing import List


class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        pass


if __name__ == "__main__":
    print(Solution().findReplaceString(S="abcd", indexes=[0, 2], sources=["a", "cd"], targets=["eee", "ffff"]))  # "eeebffff"
    print(Solution().findReplaceString(S="abcd", indexes=[0, 2], sources=["ab", "ec"], targets=["eee", "ffff"]))  # "eeecd"
