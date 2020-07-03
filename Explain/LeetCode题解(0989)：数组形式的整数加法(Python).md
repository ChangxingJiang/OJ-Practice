# LeetCode题解(0989)：数组形式的整数加法(Python)

题目：[原题链接](https://leetcode-cn.com/problems/add-to-array-form-of-integer/)（简单）

| 解法           | 时间复杂度       | 空间复杂度       | 执行用时       |
| -------------- | ---------------- | ---------------- | -------------- |
| Ans 1 (Python) | $O(max(N,logK))$ | $O(max(N,logK))$ | 351ms (81.29%) |
| Ans 2 (Python) |                  |                  |                |
| Ans 3 (Python) |                  |                  |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（逐位相加）：

```python
def addToArrayForm(self, A: List[int], K: int) -> List[int]:
    carry = 0
    ans = []
    while len(A) > 0 or K > 0 or carry > 0:
        if len(A) > 0:
            a = A.pop(-1)
        else:
            a = 0

        if K > 0:
            b = K % 10
            K //= 10
        else:
            b = 0

        t = a + b + carry
        ans.append(t % 10)
        carry = t // 10
    return ans[::-1]
```