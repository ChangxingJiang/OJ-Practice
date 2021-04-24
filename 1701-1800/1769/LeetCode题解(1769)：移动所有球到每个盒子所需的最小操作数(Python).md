# LeetCode题解(1769)：移动所有球到每个盒子所需的最小操作数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/)（中等）

标签：贪心算法、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 68ms (69.42%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        size = len(boxes)

        prefix = []  # 将前面的小球全部移动到当前位置
        last = now = 0
        for i in range(size):
            last += now
            prefix.append(last)
            if boxes[i] == "1":
                now += 1

        suffix = []  # 将后面的小球全部移动到当前位置
        last = now = 0
        for i in range(size - 1, -1, -1):
            last += now
            suffix.append(last)
            if boxes[i] == "1":
                now += 1
        suffix.reverse()

        return [prefix[i] + suffix[i] for i in range(size)]
```

