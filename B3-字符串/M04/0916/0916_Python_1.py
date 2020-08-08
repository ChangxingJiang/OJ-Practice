from typing import List


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        pass


if __name__ == "__main__":
    print(Solution().wordSubsets(A=["amazon", "apple", "facebook", "google", "leetcode"], B=["e", "o"]))  # ["facebook","google","leetcode"]
    print(Solution().wordSubsets(A=["amazon", "apple", "facebook", "google", "leetcode"], B=["l", "e"]))  # ["apple","google","leetcode"]
    print(Solution().wordSubsets(A=["amazon", "apple", "facebook", "google", "leetcode"], B=["e", "oo"]))  # ["facebook","google"]
    print(Solution().wordSubsets(A=["amazon", "apple", "facebook", "google", "leetcode"], B=["lo", "eo"]))  # ["google","leetcode"]
    print(Solution().wordSubsets(A=["amazon", "apple", "facebook", "google", "leetcode"], B=["ec", "oc", "ceo"]))  # ["facebook","leetcode"]
