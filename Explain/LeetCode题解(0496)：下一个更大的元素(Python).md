# LeetCode题解(0496)：下一个更大的元素(Python)

题目：[原题链接](https://leetcode-cn.com/problems/next-greater-element-i/)（简单）

题目标签：

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | O(N^2)     | O(N)       | 128ms (13.04%) |
| Ans 2 (Python) | O(M+N)     | O(N)       | 56ms (92.60%)  |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力解法）：

```python
def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    ans = []
    for n in nums1:
        idx = nums2.index(n)
        for m in nums2[idx:]:
            if m > n:
                ans.append(m)
                break
        else:
            ans.append(-1)
    return ans
```

解法二（单调栈）：

```python
def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    block = []
    hashmap = {}
    for n in nums2:
        while len(block) > 0:
            if n > block[-1]:
                hashmap[block.pop(-1)] = n
            else:
                break
        block.append(n)
    else:
        for n in block:
            hashmap[n] = -1

    return [hashmap[n] for n in nums1]
```