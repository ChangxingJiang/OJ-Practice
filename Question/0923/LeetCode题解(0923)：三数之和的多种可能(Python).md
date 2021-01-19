# LeetCode题解(0923)：三数之和的多种可能(Python)

题目：[原题链接](https://leetcode-cn.com/problems/3sum-with-multiplicity/)（中等）

标签：数组、双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(logN)$  | 4404ms (5.19%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    _MOD = 10 ** 9 + 7

    def threeSumMulti(self, A: List[int], target: int) -> int:
        A.sort()
        ans = 0
        for i in range(len(A)):
            j, k = i + 1, len(A) - 1
            while j <= k:
                if A[i] + A[j] + A[k] < target:
                    j += 1
                elif A[i] + A[j] + A[k] > target:
                    k -= 1
                elif A[j] != A[k]:
                    left = right = 1
                    while j + 1 < k and A[j] == A[j + 1]:
                        left += 1
                        j += 1
                    while k - 1 > j and A[k] == A[k - 1]:
                        right += 1
                        k -= 1
                    ans += left * right
                    ans %= self._MOD
                    j += 1
                    k -= 1
                else:
                    ans += (k - j + 1) * (k - j) // 2
                    ans %= self._MOD
                    break

        return ans
```

