from typing import List


class Solution:
    def multiSearch(self, big: str, smalls: List[str]) -> List[List[int]]:
        # 构造字典树
        tree = {}
        for i, word in enumerate(smalls):
            node = tree
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node["@"] = i

        s1, s2 = len(smalls), len(big)

        ans = [[] for _ in range(s1)]

        for i in range(s2):
            j = i
            node = tree
            while j < s2 and big[j] in node:
                node = node[big[j]]
                j += 1
                if "@" in node:
                    ans[node["@"]].append(i)

        return ans


if __name__ == "__main__":
    # [[1,4],[8],[],[3],[1,4,7,10],[5]]
    print(Solution().multiSearch(big="mississippi", smalls=["is", "ppi", "hi", "sis", "i", "ssippi"]))
