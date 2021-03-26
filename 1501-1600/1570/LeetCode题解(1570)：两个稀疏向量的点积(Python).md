# LeetCode题解(1570)：两个稀疏向量的点积(Python)

题目：[原题链接](https://leetcode-cn.com/problems/dot-product-of-two-sparse-vectors/)（中等）

标签：哈希表、数组、双指针

| 解法           | 时间复杂度                                                 | 空间复杂度 | 执行用时        |
| -------------- | ---------------------------------------------------------- | ---------- | --------------- |
| Ans 1 (Python) | 实例化 : $O(N)$ ; 计算 = $O(C1+C2)$（其中C为向量中值的数） | $O(C)$     | 1948ms (66.15%) |
| Ans 2 (Python) |                                                            |            |                 |
| Ans 3 (Python) |                                                            |            |                 |

解法一：

```python
class SparseVector:
    def __init__(self, nums: List[int]):
        self.array = [(i, n) for i, n in enumerate(nums) if n != 0]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        s1, s2 = len(self.array), len(vec.array)
        i1, i2 = 0, 0
        ans = 0
        while i1 < s1 and i2 < s2:
            idx1, n1 = self.array[i1]
            idx2, n2 = vec.array[i2]
            if idx1 == idx2:
                ans += n1 * n2
                i1 += 1
                i2 += 1
            elif idx1 < idx2:
                i1 += 1
            else:
                i2 += 1
        return ans
```