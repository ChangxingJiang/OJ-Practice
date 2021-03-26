# LeetCode题解(1415)：长度为n的开心字符串中字典序第k小的字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/)（中等）

标签：回溯算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(1)$     | 36ms (95.03%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = []
        for i in range(n):
            v = 2 ** (n - i - 1)
            if i == 0:
                if k > 3 * v:
                    return ""
                if k > 2 * v:
                    ans.append("c")
                    k -= 2 * v
                elif k > v:
                    ans.append("b")
                    k -= v
                else:
                    ans.append("a")
            else:
                if k > v:
                    if ans[-1] == "a" or ans[-1] == "b":
                        ans.append("c")
                    else:
                        ans.append("b")
                    k -= v
                else:
                    if ans[-1] == "b" or ans[-1] == "c":
                        ans.append("a")
                    else:
                        ans.append("b")
        return "".join(ans)
```

