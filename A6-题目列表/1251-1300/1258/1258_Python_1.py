from typing import List


class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        pass


if __name__ == "__main__":
    # ["I am cheerful today but was sad yesterday",
    # "I am cheerful today but was sorrow yesterday",
    # "I am happy today but was sad yesterday",
    # "I am happy today but was sorrow yesterday",
    # "I am joy today but was sad yesterday",
    # "I am joy today but was sorrow yesterday"]
    print(Solution().generateSentences(synonyms=[["happy", "joy"], ["sad", "sorrow"], ["joy", "cheerful"]],
                                       text="I am happy today but was sad yesterday"))
