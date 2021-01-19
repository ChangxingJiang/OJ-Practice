# LeetCode题解(0855)：考场就座(Python)

题目：[原题链接](https://leetcode-cn.com/problems/exam-room/)（中等）

标签：有序映射

| 解法           | 时间复杂度                     | 空间复杂度 | 执行用时       |
| -------------- | ------------------------------ | ---------- | -------------- |
| Ans 1 (Python) | seat = $O(N)$ ; leave = $O(N)$ | $O(N)$     | 280ms (72.41%) |
| Ans 2 (Python) |                                |            |                |
| Ans 3 (Python) |                                |            |                |

解法一：

```python
class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.students = []

    def seat(self) -> int:
        if not self.students:
            max_idx = 0
        else:
            max_idx, max_val = 0, self.students[0]
            for i, s in enumerate(self.students):
                if i > 0:
                    prev = self.students[i - 1]
                    distance = (s - prev) // 2
                    if distance > max_val:
                        max_idx, max_val = prev + distance, distance
            distance = self.n - 1 - self.students[-1]
            if distance > max_val:
                max_idx = self.n - 1
        bisect.insort_right(self.students, max_idx)
        return max_idx

    def leave(self, p: int) -> None:
        self.students.remove(p)
```

