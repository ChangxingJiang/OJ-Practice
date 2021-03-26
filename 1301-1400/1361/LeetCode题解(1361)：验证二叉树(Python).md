# LeetCode题解(1361)：验证二叉树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/validate-binary-tree-nodes/)（中等）

标签：并查集、图

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 156ms (11.67%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
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
```

