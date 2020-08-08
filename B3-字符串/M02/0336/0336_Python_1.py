from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        pass


if __name__ == "__main__":
    print(Solution().palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))  # [[0,1],[1,0],[3,2],[2,4]]
    print(Solution().palindromePairs(["bat", "tab", "cat"]))  # [[0,1],[1,0]]
