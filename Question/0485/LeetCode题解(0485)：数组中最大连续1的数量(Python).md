# LeetCode题解(0485)：数组中最大连续1的数量(Python)

题目：[原题链接](https://leetcode-cn.com/problems/max-consecutive-ones/)（简单）

题目标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | O(n)       | O(n)       | 476ms (38.77%) |
| Ans 2 (Python) | O(n)       | O(1)       | 420ms (84.49%) |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（转换为字符串处理）：

```python
def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    s = "".join([str(n) for n in nums])
    return max([len(n) for n in s.split("0")])
```

解法二（直接遍历计算）：

```python
def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    maximum = 0
    num = 0
    for n in nums:
        if n == 1:
            num += 1
        else:
            if num > maximum:
                maximum = num
            num = 0
    else:
        if num > maximum:
            maximum = num
    return maximum
```