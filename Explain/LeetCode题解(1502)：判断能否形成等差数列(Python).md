# LeetCode题解(1502)：判断能否形成等差数列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/can-make-arithmetic-progression-from-sequence/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 44ms (100.00%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（排序法）：

![LeetCode题解(1502)：截图1](LeetCode题解(1502)：截图1.png)

```python
def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
    arr.sort()
    for i in range(len(arr) - 2):
        if arr[i + 1] - arr[i] != arr[i + 2] - arr[i + 1]:
            return False
    else:
        return True
```