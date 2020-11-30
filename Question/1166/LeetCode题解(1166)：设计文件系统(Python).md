# LeetCode题解(1166)：设计文件系统(Python)

题目：[原题链接](https://leetcode-cn.com/problems/design-file-system/)（中等）

标签：设计、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(1)$     | $O(N)$     | 240ms (90.91%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class FileSystem:

    def __init__(self):
        self.hashmap = {"": -1}

    def createPath(self, path: str, value: int) -> bool:
        if path in self.hashmap:
            return False
        if path[:path.rindex("/")] not in self.hashmap:
            return False
        self.hashmap[path] = value
        return True

    def get(self, path: str) -> int:
        if path in self.hashmap:
            return self.hashmap[path]
        else:
            return -1
```

