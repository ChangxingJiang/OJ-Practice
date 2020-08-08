from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        pass


if __name__ == "__main__":
    print(Solution().findSubstring(s="barfoothefoobarman", words=["foo", "bar"]))  # [0,9]
    print(Solution().findSubstring(s="wordgoodgoodgoodbestword", words=["word", "good", "best", "word"]))  # []
