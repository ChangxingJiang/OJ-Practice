# LeetCode题解(0448)：寻找数组中缺失的数字(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | --         | --         | 412ms (92.00%) |
| Ans 2 (Python) | O(n)       | O(n)       | 388ms (99.37%) |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（Pythonic）：

```python
def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    return list(set([i for i in range(1, len(nums) + 1)]) - set(nums))
```

解法二（遍历）：

```python
def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    g = [0] * (len(nums) + 1)
    for n in nums:
        g[n] = 1
    ans = []
    for n in range(1, len(nums) + 1):
        if g[n] == 0:
            ans.append(n)
    return ans
```