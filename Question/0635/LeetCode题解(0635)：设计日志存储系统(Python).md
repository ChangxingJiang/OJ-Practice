# LeetCode题解(0635)：设计日志存储系统(Python)

题目：[原题链接](https://leetcode-cn.com/problems/design-log-storage-system/)（中等）

标签：设计、字符串

| 解法           | 时间复杂度                       | 空间复杂度 | 执行用时      |
| -------------- | -------------------------------- | ---------- | ------------- |
| Ans 1 (Python) | put = $O(1)$ ; retrieve = $O(N)$ | $O(N)$     | 48ms (96.55%) |
| Ans 2 (Python) |                                  |            |               |
| Ans 3 (Python) |                                  |            |               |

解法一：

```python
TIME_LENGTH = {
    "Year": 4,
    "Month": 7,
    "Day": 10,
    "Hour": 13,
    "Minute": 16,
    "Second": 19
}


class LogSystem:

    def __init__(self):
        self.logs = []

    def put(self, id: int, timestamp: str) -> None:
        self.logs.append((id, timestamp))

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        bits_num = TIME_LENGTH[granularity]

        ans = []
        for log in self.logs:
            if start[:bits_num] <= log[1][:bits_num] <= end[:bits_num]:
                ans.append(log[0])
        return ans
```

