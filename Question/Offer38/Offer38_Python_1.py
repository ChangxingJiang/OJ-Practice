from typing import List


class Solution:
    def __init__(self):
        self.s = []
        self.lst = []
        self.ans = set()

    def permutation(self, s: str) -> List[str]:
        self.s = list(s)

        def dfs():
            if self.s:
                for i, ch in enumerate(self.s):
                    ch = self.s.pop(i)
                    self.lst.append(ch)
                    dfs()
                    self.lst.pop()
                    self.s.insert(i, ch)
            else:
                self.ans.add("".join(self.lst))

        dfs()

        return list(self.ans)


if __name__ == "__main__":
    # ["abc","acb","bac","bca","cab","cba"]
    print(Solution().permutation("abc"))

    # ["aba","aab","baa"]
    print(Solution().permutation("aab"))
