# LeetCode题解(1585)：检查字符串是否可以通过排序子字符串得到另一个字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/check-if-string-is-transformable-with-substring-sort-operations/)（困难）

标签：贪心算法、字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时    |
| -------------- | ---------- | ---------- | ----------- |
| Ans 1 (Python) | $O(S×T)$   | $O(S+T)$   | 1720ms (9%) |
| Ans 2 (Python) |            |            |             |
| Ans 3 (Python) |            |            |             |

解法一：

```python
class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        # 计算两个字符串的字符位置
        S = collections.defaultdict(list)
        for i, ch in enumerate(s):
            S[int(ch)].append(i)
        T = collections.defaultdict(list)
        for i, ch in enumerate(t):
            T[int(ch)].append(i)

        # 每次升序只能让小的向前移动，让大的向后移动；而不能让大的向后移动
        for n in range(10):  # 遍历10个字符
            # 如果字符数量不相等则直接报错
            if len(S[n]) != len(T[n]):
                return False

            # 检查是否可以通过排序生成
            last_idx1 = 0
            last_idx2 = 0
            total_num1 = 0
            total_num2 = 0
            for i in range(len(S[n])):
                idx1 = S[n][i]
                idx2 = T[n][i]
                total_num1 += sum([1 if int(s[j]) < n else 0 for j in range(last_idx1, idx1)])
                total_num2 += sum([1 if int(t[j]) < n else 0 for j in range(last_idx2, idx2)])
                if total_num1 > total_num2:
                    # print("错误原因:", n, S[n], T[n])
                    return False
                last_idx1, last_idx2 = idx1, idx2

        return True
```