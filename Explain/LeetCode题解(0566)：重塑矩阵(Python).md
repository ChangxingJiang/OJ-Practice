# LeetCode题解(0566)：重塑矩阵(Python)

题目：[原题链接](https://leetcode-cn.com/problems/reshape-the-matrix/)（简单）

题目标签：

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 124ms (53.77%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 120ms (68.18%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力解法）：

```python
def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
    total = []
    for n in nums:
        for m in n:
            total.append(m)

    size = len(total)
    if r * c != size:
        return nums

    ans = []
    for i in range(r):
        ans.append(total[i * c: i * c + c])
    return ans
```

解法二（在遍历同时生成结果）：

```python
def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
    temp = []
    ans = []
    for n in nums:
        for m in n:
            temp.append(m)
            if len(temp) == c:
                ans.append(temp)
                temp = []
    else:
        if len(temp) == c:
            ans.append(temp)
        elif len(temp) != 0:
            return nums
    if len(ans) == r:
        return ans
    else:
        return nums
```