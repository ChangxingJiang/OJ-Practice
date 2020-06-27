# LeetCode题解(0349)：求两个数组的交集(Python)

题目：[原题链接](https://leetcode-cn.com/problems/intersection-of-two-arrays/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | --         | --         | 56ms (85.78%) |
| Ans 2 (Python) | O(n^2)     | O(n)       | 84ms (28.84%) |
| Ans 3 (Python) | O(m+n)     | O(m+n)     | 88ms (23.15%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（Pythonic）：

```python
def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    return list(set(nums1) & set(nums2))
```

解法二（迭代）：

```python
def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    ans = []
    for n in nums2:
        if n in nums1 and n not in ans:
            ans.append(n)
    return ans
```

解法三（两个set）：

```python
def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    nums1 = set(nums1)
    nums2 = set(nums2)
    if len(nums1) < len(nums2):
        return [x for x in nums2 if x in nums1]
    else:
        return [x for x in nums1 if x in nums2]
```