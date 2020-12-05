# LeetCode题解(0497)：非重叠矩形中的随机点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/random-point-in-non-overlapping-rectangles/)（中等）

标签：随机、二分查找

| 解法           | 时间复杂度        | 空间复杂度 | 执行用时       |
| -------------- | ----------------- | ---------- | -------------- |
| Ans 1 (Python) | 每次抽取 = $O(N)$ | $O(N)$     | 164ms (98.48%) |
| Ans 2 (Python) |                   |            |                |
| Ans 3 (Python) |                   |            |                |

解法一：

```python
class Solution:
    # 非重叠、轴对齐矩形

    def __init__(self, rects: List[List[int]]):
        self.rects = rects

        self.part = []
        for rect in rects:
            size = (rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1)
            self.part.append(size)
        self.total = sum(self.part)

    def pick(self) -> List[int]:
        target = random.randint(1, self.total)  # 随机按面积为权重选择矩形

        now = 0
        for i, size in enumerate(self.part):
            if now + size >= target:
                x1, y1, x2, y2 = self.rects[i]
                a, b = divmod(target - now - 1, x2 - x1 + 1)
                # print(x1, y1, x2, y2, ":", target - now - 1, x2 - x1 + 1, "->", a, b)
                return [x1 + b, y1 + a]
            else:
                now += size
```