# LeetCode题解(0604)：迭代压缩字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/design-compressed-string-iterator/)（简单）

标签：设计、字符串

| 解法           | 时间复杂度                    | 空间复杂度 | 执行用时      |
| -------------- | ----------------------------- | ---------- | ------------- |
| Ans 1 (Python) | 构造 = $O(S)$ ; 查询 = $O(1)$ | $O(S)$     | 52ms (89.69%) |
| Ans 2 (Python) |                               |            |               |
| Ans 3 (Python) |                               |            |               |

解法一：

```python
class StringIterator:

    def __init__(self, compressedString: str):
        temp = []
        for ch in compressedString:
            if ch.isnumeric() and temp and temp[-1].isnumeric():
                temp[-1] += ch
            else:
                temp.append(ch)

        self.lst = collections.deque()
        for i in range(len(temp) // 2):
            self.lst.append([temp[2 * i], int(temp[2 * i + 1])])

    def next(self) -> str:
        if self.lst:
            val = self.lst[0][0]
            self.lst[0][1] -= 1
            if self.lst[0][1] == 0:
                self.lst.popleft()
            return val
        else:
            return " "

    def hasNext(self) -> bool:
        return len(self.lst) > 0
```