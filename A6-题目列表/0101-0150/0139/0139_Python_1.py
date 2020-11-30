from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().wordBreak(s="leetcode", wordDict=["leet", "code"]))  # True
    print(Solution().wordBreak(s="applepenapple", wordDict=["apple", "pen"]))  # True
    print(Solution().wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))  # False
