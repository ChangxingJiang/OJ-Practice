# LeetCode题解(1480)：一维数组的动态和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/running-sum-of-1d-array/)（简单）

标签：数组遍历

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 36ms (90.54%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def runningSum(self, nums: List[int]) -> List[int]:
    now = 0
    ans = []
    for n in nums:
        now += n
        ans.append(now)
    return ans
```