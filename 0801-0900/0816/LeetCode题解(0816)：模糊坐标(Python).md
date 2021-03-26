# LeetCode题解(0816)：计算没有,和.的坐标的所有可能(Python)

题目：[原题链接](https://leetcode-cn.com/problems/ambiguous-coordinates/)（中等）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^3)$   | $O(1)$     | 60ms (73.91%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def ambiguousCoordinates(self, S: str) -> List[str]:
        # 转换为小数格式（如无法转换则返回None）
        def change_to_num(n1, n2):
            if int(n1) > 0 and n1[0] == "0":
                return None
            if int(n1) == 0 and len(n1) > 1:
                return None
            if n2 and (int(n2) == 0 or n2[-1] == "0"):
                return None
            if not n2:
                return n1
            else:
                return n1 + "." + n2

        S = S[1:-1]

        ans = []

        for i in range(1, len(S)):
            a = S[:i]
            b = S[i:]
            for j in range(1, len(a) + 1):
                aa = change_to_num(a[:j], a[j:])
                if aa:
                    for k in range(1, len(b) + 1):
                        bb = change_to_num(b[:k], b[k:])
                        if bb:
                            ans.append("(" + aa + ", " + bb + ")")
        return ans
```