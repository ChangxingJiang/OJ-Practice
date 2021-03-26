from typing import List


class Solution:
    def __init__(self):
        self.ans = []
        self.lst = []
        self.now = []

    def permutation(self, S: str) -> List[str]:
        self.lst = list(S)
        self.count()
        return ["".join(e) for e in self.ans if e]

    def count(self):
        if len(self.now) == len(self.lst):
            self.ans.append(list(self.now))
        else:
            for ch in self.lst:
                if ch not in self.now:
                    self.now.append(ch)
                    self.count()
                    self.now.pop()


if __name__ == "__main__":
    # ["qwe", "qew", "wqe", "weq", "ewq", "eqw"]
    print(Solution().permutation("qwe"))

    # ["ab", "ba"]
    print(Solution().permutation("ab"))
