from typing import List


class DSU1:
    def __init__(self, n: int):
        self._n = n
        self._array = [i for i in range(n)]
        self._size = [1] * n

    def find(self, i: int):
        if self._array[i] != i:
            self._array[i] = self.find(self._array[i])
        return self._array[i]

    def union(self, i: int, j: int):
        i, j = self.find(i), self.find(j)
        if self._size[i] >= self._size[j]:
            self._array[j] = i
            self._size[i] += self._size[j]
        else:
            self._array[i] = j
            self._size[j] += self._size[i]

    def group_num(self):
        groups = set()
        for i in range(len(self._array)):
            if self._array[i] not in groups:
                j = self.find(i)
                if j not in groups:
                    groups.add(self.find(i))
        return len(groups)

    def __repr__(self):
        return str(len(self._array)) + ":" + str(self._array)


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        dsu = DSU1(n)
        for i in range(n):
            if leftChild[i] != -1:
                if dsu.find(i) == dsu.find(leftChild[i]):
                    return False
                else:
                    dsu.union(i, leftChild[i])
            if rightChild[i] != -1:
                if dsu.find(i) == dsu.find(rightChild[i]):
                    return False
                else:
                    dsu.union(i, rightChild[i])
        return dsu.group_num() == 1


if __name__ == "__main__":
    # True
    print(Solution().validateBinaryTreeNodes(n=4,
                                             leftChild=[1, -1, 3, -1],
                                             rightChild=[2, -1, -1, -1]))

    print(Solution().validateBinaryTreeNodes(n=4, leftChild=[1, -1, 3, -1], rightChild=[2, 3, -1, -1]))  # False

    # True
    print(Solution().validateBinaryTreeNodes(n=4,
                                             leftChild=[3, -1, 1, -1],
                                             rightChild=[-1, -1, 0, -1]))

    print(Solution().validateBinaryTreeNodes(n=2, leftChild=[1, 0], rightChild=[-1, -1]))  # False

    # False
    print(Solution().validateBinaryTreeNodes(n=6,
                                             leftChild=[1, -1, -1, 4, -1, -1],
                                             rightChild=[2, -1, -1, 5, -1, -1]))
