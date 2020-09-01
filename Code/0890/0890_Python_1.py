from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            if len(word) != len(pattern):
                continue
            mapping = {}
            values = set()
            for i in range(len(word)):
                if word[i] not in mapping:
                    if pattern[i] in values:
                        break
                    else:
                        mapping[word[i]] = pattern[i]
                        values.add(pattern[i])
                elif mapping[word[i]] != pattern[i]:
                    break
            else:
                ans.append(word)
        return ans


if __name__ == "__main__":
    print(Solution().findAndReplacePattern(words=["abc", "deq", "mee", "aqq", "dkd", "ccc"], pattern="abb"))  # ["mee","aqq"]
