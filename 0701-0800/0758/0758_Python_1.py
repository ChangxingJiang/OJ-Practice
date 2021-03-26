from typing import List


class Solution:
    def boldWords(self, words: List[str], S: str) -> str:
        # 构造字典树
        tree = {}
        for word in words:
            node = tree
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node["@"] = ""

        # 使用字典树
        lst = [False] * len(S)
        for i in range(len(S)):
            m = i
            n = -1
            node = tree
            while m < len(S) and S[m] in node:
                node = node[S[m]]
                if "@" in node:
                    n = m
                m += 1

            if n != -1:
                for j in range(i, n + 1):
                    lst[j] = True

        ans = []

        for i in range(len(S)):
            if lst[i] is True and (i == 0 or lst[i - 1] is False):
                ans.append("<b>")
            ans.append(S[i])
            if lst[i] is True and (i == len(S) - 1 or lst[i + 1] is False):
                ans.append("</b>")

        return "".join(ans)


if __name__ == "__main__":
    # a<b>abc</b>d
    # print(Solution().boldWords(words=["ab", "bc"], S="aabcd"))

    # eeaa<b>d</b>a<b>d</b>a<b>dc</b>
    print(Solution().boldWords(words=["ccb", "b", "d", "cba", "dc"], S="eeaadadadc"))
