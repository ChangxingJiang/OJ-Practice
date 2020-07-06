from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for i1 in range(len(words)):
            word1 = words[i1]
            for i2 in range(len(words)):
                word2 = words[i2]
                if i1 != i2 and word1 in word2:
                    ans.append(word1)
                    break
        return ans


if __name__ == "__main__":
    print(Solution().stringMatching(words=["mass", "as", "hero", "superhero"]))  # ["as","hero"]
    print(Solution().stringMatching(words=["leetcode", "et", "code"]))  # ["et","code"]
    print(Solution().stringMatching(words=["blue", "green", "bu"]))  # []
