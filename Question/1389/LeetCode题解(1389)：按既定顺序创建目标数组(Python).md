# LeetCode题解(1389)：按既定顺序创建目标数组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/create-target-array-in-the-given-order/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(1)$     | 36ms (87.34%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
    target = []
    for i in range(len(nums)):
        target.insert(index[i], nums[i])
    return target
```