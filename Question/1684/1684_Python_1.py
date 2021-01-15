from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        allowed = set(allowed)
        for word in words:
            word = set(word)
            if word <= allowed:
                ans += 1
        return ans


if __name__ == "__main__":
    print(Solution().countConsistentStrings(allowed="ab", words=["ad", "bd", "aaab", "baa", "badab"]))  # 2
    print(Solution().countConsistentStrings(allowed="abc", words=["a", "b", "c", "ab", "ac", "bc", "abc"]))  # 7
    print(
        Solution().countConsistentStrings(allowed="cad", words=["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]))  # 4
