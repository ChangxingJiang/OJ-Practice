# LeetCode题解(1625)：执行指定操作后字典序最小的字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/lexicographically-smallest-string-after-applying-operations/)（中等）

标签：数学、深度优先搜索、广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时    |
| -------------- | ---------- | ---------- | ----------- |
| Ans 1 (Python) | $O(S)$     | $O(S)$     | 124ms (93%) |
| Ans 2 (Python) |            |            |             |
| Ans 3 (Python) |            |            |             |

解法一：

```python
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        # a的可累加数量
        maybe_a_lst = {
            1: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            2: [0, 2, 4, 6, 8],
            3: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            4: [0, 2, 4, 6, 8],
            5: [0, 5],
            6: [0, 2, 4, 6, 8],
            7: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            8: [0, 2, 4, 6, 8],
            9: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        }

        # b的可轮转数量
        maybe_b_list = {0}
        last = 0
        while True:
            last += b
            last %= len(s)
            if last not in maybe_b_list:
                maybe_b_list.add(last)
            else:
                break

        # 轮转为偶数的情况
        if b % 2 == 0:
            ans = s
            for i in maybe_b_list:
                # 计算第二个奇数位的增加量
                add_2, min_2 = 0, a
                for aa in maybe_a_lst[a]:
                    val = (int(s[(i + 1) % len(s)]) + aa) % 10
                    if val < min_2:
                        add_2, min_2 = aa, val

                # 计算转换结果
                now = []
                for j in range(i, i + len(s)):
                    j %= len(s)
                    if j % 2 == 0:
                        now.append(s[j])
                    else:
                        now.append(str((int(s[j]) + add_2) % 10))
                now = "".join(now)
                ans = min(ans, now)

        # 轮转为奇数的情况
        else:
            ans = s
            for i in maybe_b_list:
                # 计算第一个奇数位的增加量
                add_1, min_1 = 0, a
                for aa in maybe_a_lst[a]:
                    val = (int(s[i]) + aa) % 10
                    if val < min_1:
                        add_1, min_1 = aa, val

                # 计算第二个奇数位的增加量
                add_2, min_2 = 0, a
                for aa in maybe_a_lst[a]:
                    val = (int(s[(i + 1) % len(s)]) + aa) % 10
                    if val < min_2:
                        add_2, min_2 = aa, val

                # 计算转换结果
                now = []
                for j in range(i, i + len(s)):
                    if (j - i) % 2 == 0:
                        j %= len(s)
                        now.append(str((int(s[j]) + add_1) % 10))
                    else:
                        j %= len(s)
                        now.append(str((int(s[j]) + add_2) % 10))
                now = "".join(now)
                ans = min(ans, now)

        return ans
```