# LeetCode题解(1429)：第一个唯一数字(Python)

题目：[原题链接](https://leetcode-cn.com/problems/first-unique-number/)（中等）

标签：设计、哈希表

| 解法           | 时间复杂度                                             | 空间复杂度 | 执行用时       |
| -------------- | ------------------------------------------------------ | ---------- | -------------- |
| Ans 1 (Python) | 构造 = $O(N)$ ; 查询 = $O(1)$ ; 增加 = $O(1)*$（摊销） | $O(N)$     | 376ms (89.02%) |
| Ans 2 (Python) |                                                        |            |                |
| Ans 3 (Python) |                                                        |            |                |

解法一（双端队列节省空间）：

```python
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.count = collections.Counter(nums)
        self.array = collections.deque(nums)
        self.first = -1
        self._find()

    def showFirstUnique(self) -> int:
        return self.first

    def add(self, value: int) -> None:
        self.count[value] += 1
        self.array.append(value)
        if self.first == -1 or value == self.first:
            self._find()

    def _find(self):
        self.first = -1
        while self.array:
            first = self.array.popleft()
            if self.count[first] == 1:
                self.first = first
                break
```