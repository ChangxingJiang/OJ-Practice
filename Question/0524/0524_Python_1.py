from typing import List


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key=lambda x: (-len(x), x))
        for word in d:
            i1 = i2 = 0
            while i1 < len(word) and i2 < len(s):
                if s[i2] == word[i1]:
                    i1 += 1
                    i2 += 1
                else:
                    i2 += 1
            if i1 == len(word):
                return word
        return ""


if __name__ == "__main__":
    print(Solution().findLongestWord(s="abpcplea", d=["ale", "apple", "monkey", "plea"]))  # apple
    print(Solution().findLongestWord(s="abpcplea", d=["a", "b", "c"]))  # a
