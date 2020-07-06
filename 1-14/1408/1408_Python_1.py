from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        pass


if __name__ == "__main__":
    print(Solution().stringMatching(words=["mass", "as", "hero", "superhero"]))  # ["as","hero"]
    print(Solution().stringMatching(words=["leetcode", "et", "code"]))  # ["et","code"]
    print(Solution().stringMatching(words=["blue", "green", "bu"]))  # []
