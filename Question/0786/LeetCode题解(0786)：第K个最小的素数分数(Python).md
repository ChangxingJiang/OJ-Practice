# LeetCode题解(0786)：第K个最小的素数分数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/k-th-smallest-prime-fraction/)（困难）

标签：堆、二分查找

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(AlogN)$ | $O(1)$     | 148ms (99.40%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（二分查找）：

```python
class Solution:
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        # 处理特殊情况
        if len(A) == 2:
            return A

        # 滑动窗口计算数量
        def count(guess):
            total = 0
            l = 0
            m_v, m_g = 1, []  # 存储略小于查询值的那一个分数
            for r in range(len(A)):
                while l < r:
                    v = A[l] / A[r]
                    # if guess <= v < m_v:
                    #     m_v, m_g = v, [A[l], A[r]]
                    if v >= guess:
                        if v < m_v:
                            m_v, m_g = v, [A[l], A[r]]
                        break
                    l += 1
                # print(l, r, A[l], A[r])
                total += r - l

            # 如果所有值都比目标值大，则选取最接近目标值的数
            if m_v == 0:
                m_g = [A[0], A[-1]]

            return total, m_g

        size = len(A)

        # 计算第K小的数时第几大的数
        T = size * (size - 1) // 2 - K + 1

        left, right = 0, 1
        for i in range(1000):  # 最多二分查找1000次
            mid = (left + right) / 2
            res, min_group = count(mid)
            # print(left, right, "->", mid, "=", res)
            if res > T:  # 如果比mid大的数多于目标值，说明mid小了
                left = mid
            elif res < T:  # 如果比mid大的数少于目标值，说明mid大了
                right = mid
            else:
                return min_group
```