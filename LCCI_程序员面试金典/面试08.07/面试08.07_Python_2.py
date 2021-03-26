from typing import List


class Solution:
    def __init__(self):
        self.lst = set()
        self.size = 0

        self.ans = []

        self.now = []

    def permutation(self, S: str) -> List[str]:
        self.lst = set(S)
        self.size = len(self.lst)

        self.count()

        return ["".join(e) for e in self.ans if e]

    def count(self):
        if len(self.now) == self.size:
            self.ans.append(list(self.now))
        else:
            for ch in list(self.lst):
                self.lst.remove(ch)
                self.now.append(ch)
                self.count()
                self.now.pop()
                self.lst.add(ch)


if __name__ == "__main__":
    # ["qwe", "qew", "wqe", "weq", "ewq", "eqw"]
    print(Solution().permutation("qwe"))

    # ["ab", "ba"]
    print(Solution().permutation("ab"))
