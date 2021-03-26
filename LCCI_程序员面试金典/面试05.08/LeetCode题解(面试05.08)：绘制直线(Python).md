# LeetCode题解(面试05.08)：绘制直线(Python)

题目：[原题链接](https://leetcode-cn.com/problems/draw-line-lcci/)（中等）

标签：位运算

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 96ms (24.00%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def drawLine(self, length: int, w: int, x1: int, x2: int, y: int) -> List[int]:
        height = length * 32 // w
        width = w // 32
        # print("高度:", height)

        ans = []

        for i in range(height):
            if i == y:
                line = []

                total = (2 ** (x2 - x1 + 1) - 1) << (w - x2 - 1)

                for _ in range(width):
                    # print(bin(total))
                    # 处理正数的情况
                    if not (total >> 31) & 1:
                        # print("处理正数:", total & ((1 << 31) - 1))
                        line.append(total & ((1 << 31) - 1))
                    # 处理负数的情况
                    else:
                        # print("处理负数:", total & ((1 << 31) - 1), (1 << 31))
                        line.append((total & ((1 << 31) - 1)) - (1 << 31))
                    total >>= 32
                ans += line[::-1]

            else:
                ans += [0] * width

        return ans
```