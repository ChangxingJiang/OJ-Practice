# LeetCode题解(0295)：数据流的中位数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-median-from-data-stream/)（困难）

标签：二分查找、设计

| 解法           | 时间复杂度                               | 空间复杂度 | 执行用时       |
| -------------- | ---------------------------------------- | ---------- | -------------- |
| Ans 1 (Python) | addNum = $O(logN)$ ; findMedian = $O(1)$ | $O(N)$     | 276ms (41.51%) |
| Ans 2 (Python) |                                          |            |                |
| Ans 3 (Python) |                                          |            |                |

解法一（二分查找）：

```python
import bisect


class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        bisect.insort_left(self.arr, num)

    def findMedian(self) -> float:
        a = len(self.arr) // 2
        b = (len(self.arr) - 1) // 2
        return (self.arr[a] + self.arr[b]) / 2
```