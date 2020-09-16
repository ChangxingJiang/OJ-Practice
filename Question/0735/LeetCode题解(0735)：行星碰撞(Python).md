# LeetCode题解(0735)：行星碰撞(Python)

题目：[原题链接](https://leetcode-cn.com/problems/asteroid-collision/)（中等）

标签：栈

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 112ms (98.04%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（栈）：

```python
def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    stack = []
    for weight in asteroids:
        if weight > 0:
            stack.append(weight)
        else:
            while stack and stack[-1] > 0:
                if stack[-1] < -weight:
                    stack.pop()
                elif stack[-1] == -weight:
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(weight)
    return stack
```