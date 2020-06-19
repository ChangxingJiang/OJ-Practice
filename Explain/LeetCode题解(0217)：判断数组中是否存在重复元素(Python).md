# LeetCode题解(0217)：判断数组中是否存在重复元素(Python)

题目：[原题链接](https://leetcode-cn.com/problems/contains-duplicate/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | --         | --         | 48ms (>67.94%) |
| Ans 2 (Python) | O(n)       | O(n)       | 48ms (>67.94%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（非常Pythonic的答案）：

```python
def containsDuplicate(self, nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)
```

解法二（使用集合暂存结果）：

```python
def containsDuplicate(self, nums: List[int]) -> bool:
    hashset = set()
    for n in nums:
        if n not in hashset:
            hashset.add(n)
        else:
            return True
    else:
        return False
```