# LeetCode题解(1694)：重新格式化电话号码(Python)

题目：[原题链接](https://leetcode-cn.com/problems/reformat-phone-number/)（简单）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 40ms (55.67%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def reformatNumber(self, number: str) -> str:
        lst = [n for n in number if n.isnumeric()]

        idx, size = 0, len(lst)

        ans = []
        while size - idx > 4:
            ans.append("".join(lst[idx:idx + 3]))
            ans.append("-")
            idx += 3

        if size - idx <= 3:
            ans.append("".join(lst[idx:]))
        else:
            ans.append("".join(lst[idx:idx + 2]))
            ans.append("-")
            ans.append("".join(lst[idx + 2:]))

        return "".join(ans)
```

