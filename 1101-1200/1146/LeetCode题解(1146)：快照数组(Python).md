# LeetCode题解(1146)：快照数组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/snapshot-array/)（中等）

标签：数组、设计

| 解法           | 时间复杂度                                                   | 空间复杂度 | 执行用时       |
| -------------- | ------------------------------------------------------------ | ---------- | -------------- |
| Ans 1 (Python) | 构造 = $O(L)$ ; set = $O(1)$ ; snap = $O(1)$ ; get = $O(logN)$ | $O(N)$     | 684ms (13.58%) |
| Ans 2 (Python) |                                                              |            |                |
| Ans 3 (Python) |                                                              |            |                |

解法一：

```python
class SnapshotArray:

    def __init__(self, length: int):
        self.lst = [[[0, 0]] for _ in range(length)]
        self.now = 0

    def set(self, index: int, val: int) -> None:
        if self.lst[index][-1][0] == self.now:
            self.lst[index][-1][1] = val
        else:
            self.lst[index].append([self.now, val])

    def snap(self) -> int:
        self.now += 1
        return self.now - 1

    def get(self, index: int, snap_id: int) -> int:
        lst = self.lst[index]
        l, r = 0, len(lst)
        while l < r:
            m = (l + r) // 2
            if lst[m][0] <= snap_id:
                l = m + 1
            else:
                r = m
        return lst[l - 1][1]
```

