# LeetCode题解(0380)：常数时间插入、删除和获取随机元素(Python)

题目：[原题链接](https://leetcode-cn.com/problems/insert-delete-getrandom-o1/)（中等）

标签：设计、哈希表、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(1)$     | $O(N)$     | 112ms (93.65%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（动态数组）：

```python
class RandomizedSet:

    def __init__(self):
        self.hashmap = {}
        self.array = []

    def insert(self, val: int) -> bool:
        if val not in self.hashmap:
            self.hashmap[val] = len(self.array)
            self.array.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.hashmap:
            idx = self.hashmap[val]
            del self.hashmap[val]
            if idx == len(self.array) - 1:
                self.array.pop()
            else:
                end = self.array.pop()
                self.array[idx] = end
                self.hashmap[end] = idx
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.array)
```