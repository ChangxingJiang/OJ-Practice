# LeetCode题解(0946)：依据push和pop序列验证是否可能是空栈操作的结果(Python)

题目：[原题链接](https://leetcode-cn.com/problems/validate-stack-sequences/)（中等）

标签：栈、情景模拟

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 32ms (100.00%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（情景模拟）：

![LeetCode题解(0946)：截图1](LeetCode题解(0946)：截图1.png)

```python
def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
    stack = []
    size = len(pushed)
    idx = 0
    for elem in popped:
        if stack and stack[-1] == elem:
            stack.pop()
        else:
            while idx < size and pushed[idx] != elem:
                stack.append(pushed[idx])
                idx += 1
            if idx >= size:
                return False
            else:
                idx += 1
    return True
```