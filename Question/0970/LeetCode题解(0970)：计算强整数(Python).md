# LeetCode题解(0970)：计算强整数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/powerful-integers/)（简单）

这题不是异或是次方，当成异或真的很坑人。

| 解法           | 时间复杂度  | 空间复杂度 | 执行用时      |
| -------------- | ----------- | ---------- | ------------- |
| Ans 1 (Python) | $O(log^2N)$ | $O(N)$     | 44ms (70.52%) |
| Ans 2 (Python) |             |            |               |
| Ans 3 (Python) |             |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（枚举解法）：

```python
def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
    ans = set()
    for i in range(20):
        pi = pow(x, i)
        if pi > bound:
            break
        for j in range(20):
            pj = pow(y, j)
            if pj > bound:
                break
            t = pi + pj
            if t > bound:
                break
            ans.add(t)

    return list(ans)
```