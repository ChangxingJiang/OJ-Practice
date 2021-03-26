from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not wordDict:
            return []

        word_set = set(wordDict)
        size = max(len(word) for word in word_set)

        def dfs(s1):
            ans = []

            if s1 in word_set:
                ans.append(s1)

            for i in range(1, len(s1)):
                if s1[:i] in word_set:
                    for s2 in dfs(s1[i:]):
                        ans.append(s1[:i] + " " + s2)
                if i > size:
                    break

            return ans

        return dfs(s)


if __name__ == "__main__":
    # [
    #   "cats and dog",
    #   "cat sand dog"
    # ]
    print(Solution().wordBreak(s="catsanddog",
                               wordDict=["cat", "cats", "and", "sand", "dog"]))

    # [
    #   "pine apple pen apple",
    #   "pineapple pen apple",
    #   "pine applepen apple"
    # ]
    print(Solution().wordBreak(s="pineapplepenapple",
                               wordDict=["apple", "pen", "applepen", "pine", "pineapple"]))

    # []
    print(Solution().wordBreak(s="catsandog",
                               wordDict=["cats", "dog", "sand", "and", "cat"]))

    # []
    print(Solution().wordBreak(s="a",wordDict=[]))
