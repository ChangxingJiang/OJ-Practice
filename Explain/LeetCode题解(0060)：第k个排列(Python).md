# LeetCode题解(0060)：计算1到n的按大小顺序的第k个排列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/permutation-sequence/submissions/)（中等）

标签：数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 48ms (37.08%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 40ms (81.55%) |
| Ans 3 (Python) |            |            |               |

解法一（递归）：

```python
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        lst = [str(i) for i in range(1, n + 1)]

        def build(nn, kk):
            # 处理已经完成递归的情况
            if nn == 1:
                return [lst.pop()]

            # 处理当前最靠前的一位
            num = math.factorial(nn - 1)  # 第一位每变化一次需要的序列数
            idx = kk // num  # 第一位的数值坐标
            return [lst.pop(idx)] + build(nn - 1, kk % num)

        return "".join(build(n, k - 1))
```

解法二（迭代）：

```python
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        lst = [str(i) for i in range(1, n + 1)]
        ans = []
        k -= 1

        while n > 1:
            num = math.factorial(n - 1)
            idx = k // num  # 第一位的数值坐标
            ans.append(lst.pop(idx))
            n -= 1
            k %= num
        ans.append(lst.pop())

        return "".join(ans)
```