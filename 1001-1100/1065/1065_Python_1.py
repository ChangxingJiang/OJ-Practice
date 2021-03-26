from typing import List


class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        tree = {}
        for i, word in enumerate(words):
            node = tree
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node["@"] = i

        ans = []
        for i in range(len(text)):
            node = tree
            j = i
            while j < len(text) and text[j] in node:
                node = node[text[j]]
                if "@" in node:
                    ans.append([i, j])
                j += 1

        return ans


if __name__ == "__main__":
    # [[3,7],[9,13],[10,17]]
    print(Solution().indexPairs(text="thestoryofleetcodeandme", words=["story", "fleet", "leetcode"]))

    # [[0,1],[0,2],[2,3],[2,4]]
    print(Solution().indexPairs(text="ababa", words=["aba", "ab"]))
