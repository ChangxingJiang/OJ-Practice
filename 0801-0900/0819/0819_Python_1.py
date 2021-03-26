import re
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        hashmap = {}
        for word in re.split("[ ,.?!]", paragraph.lower()):
            word = "".join(list(filter(str.isalpha, word)))
            if len(word) > 0:
                if word not in hashmap:
                    hashmap[word] = 1
                else:
                    hashmap[word] += 1

        banned = set(banned)
        times = 0
        ans = ""
        for key, value in hashmap.items():
            if value > times and key not in banned:
                ans = key
                times = value
        return ans


if __name__ == "__main__":
    print(Solution().mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))  # ball
    print(Solution().mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"]))  # b
