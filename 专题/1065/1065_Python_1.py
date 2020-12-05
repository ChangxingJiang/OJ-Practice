from typing import List


class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        pass


if __name__ == "__main__":
    # [[3,7],[9,13],[10,17]]
    print(Solution().indexPairs(text="thestoryofleetcodeandme", words=["story", "fleet", "leetcode"]))

    # [[0,1],[0,2],[2,3],[2,4]]
    print(Solution().indexPairs(text="ababa", words=["aba", "ab"]))
