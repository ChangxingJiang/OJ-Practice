# LeetCode题解(0402)：移除k位数字使剩下的数字最小(Python)

题目：[原题链接](https://leetcode-cn.com/problems/remove-k-digits/)（中等）

标签：栈、贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 48ms (74.57%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（栈+贪心算法）：

```python
def removeKdigits(self, num: str, k: int) -> str:
    stack = []

    # 使用栈使每一位获得最小值
    for ch in num:
        n = int(ch)
        while k > 0 and stack and stack[-1] > n:
            stack.pop()
            k -= 1
        if stack != [] or n != 0:
            stack.append(n)

    # 处理没有被用掉的k
    while k > 0 and stack:
        stack.pop()
        k -= 1

    # 返回结果（若空栈则返回0）
    return "".join([str(n) for n in stack]) if stack else "0"
```