from typing import List


class DSU2:
    def __init__(self):
        self._n = 0
        self._parent = {}
        self._size = {}

    def __contains__(self, i):
        return i in self._parent

    def add(self, i):
        if i not in self._parent:
            self._parent[i] = i
            self._size[i] = 1

    def get_size(self, i):
        return self._size[self.find(i)]

    def find(self, i):
        if self._parent[i] != i:
            self._parent[i] = self.find(self._parent[i])
        return self._parent[i]

    def union(self, i, j):
        i, j = self.find(i), self.find(j)
        if i != j:
            self._parent[i] = j
            self._size[j] += self._size[i]
            del self._size[i]

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        dsu = DSU2()

        for equation in equations:
            if "==" in equation:
                n1, n2 = equation.split("==")
                if n1 not in dsu:
                    dsu.add(n1)
                if n2 not in dsu:
                    dsu.add(n2)
                dsu.union(n1, n2)

        for equation in equations:
            if "!=" in equation:
                n1, n2 = equation.split("!=")
                if n1 not in dsu:
                    dsu.add(n1)
                if n2 not in dsu:
                    dsu.add(n2)
                if dsu.find(n1) == dsu.find(n2):
                    return False

        return True


if __name__ == "__main__":
    print(Solution().equationsPossible(["a==b", "b!=a"]))  # False
    print(Solution().equationsPossible(["b==a", "a==b"]))  # True
    print(Solution().equationsPossible(["a==b", "b==c", "a==c"]))  # True
    print(Solution().equationsPossible(["a==b", "b!=c", "c==a"]))  # False
    print(Solution().equationsPossible(["c==c", "b==d", "x!=z"]))  # True
