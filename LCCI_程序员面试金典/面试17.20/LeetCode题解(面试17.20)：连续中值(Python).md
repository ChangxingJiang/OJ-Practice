# LeetCode题解(面试17.20)：连续中值(Python)

题目：[原题链接](https://leetcode-cn.com/problems/continuous-median-lcci/)（困难）

标签：设计、堆

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(1)$     | $O(N)$     | 248ms (69.47%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class MedianFinder:

    def __init__(self):
        self.heap_smaller = []  # 小于中位数的值
        self.heap_bigger = []  # 大于中位数的值
        self.mid = []  # 中位数
        self.n = 0  # 数列数的总数

    def addNum(self, num: int) -> None:
        # 处理第1个传入的数的情况
        if self.n == 0:
            self.mid.append(num)

        # 处理第2个传入的数的情况
        elif self.n == 1:
            self.mid.append(num)

        # 处理第3个传入的数的情况
        elif self.n == 2:
            mid1, mid2, mid3 = sorted(self.mid + [num])
            heapq.heappush(self.heap_smaller, -mid1)
            heapq.heappush(self.heap_bigger, mid3)
            self.mid = [mid2]

        # 处理第4,6,8,...个传入的数的情况
        elif self.n % 2 == 1:
            mid1, mid3 = sorted(self.mid + [num])

            if -mid1 > self.heap_smaller[0]:
                mid1 = -heapq.heappushpop(self.heap_smaller, -mid1)
            if mid3 > self.heap_bigger[0]:
                mid3 = heapq.heappushpop(self.heap_bigger, mid3)

            self.mid = [mid1, mid3]

        # 处理第5,7,9,...个传入的数的情况
        else:
            mid1, mid2, mid3 = sorted(self.mid + [num])

            if -mid1 > self.heap_smaller[0]:
                mid1 = -heapq.heappushpop(self.heap_smaller, -mid1)
            if mid3 > self.heap_bigger[0]:
                mid3 = heapq.heappushpop(self.heap_bigger, mid3)

            heapq.heappush(self.heap_smaller, -mid1)
            heapq.heappush(self.heap_bigger, mid3)
            self.mid = [mid2]

        self.n += 1

    def findMedian(self) -> float:
        return sum(self.mid) / len(self.mid) if self.mid else float("NAN")
```