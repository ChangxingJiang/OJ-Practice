# LeetCode题解(0306)：累加数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/additive-number/)（中等）

标签：回溯算法、字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^3)$   | $O(N)$     | 36ms (86.49%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        for i in range(1, len(num) // 2 + 1):  # 长度可能接近一半：1991+1=1992
            for j in range(i + 1, i + (len(num) - i) // 2 + 1):
                v1, v2 = int(num[:i]), int(num[i:j])
                # 不能为0开头
                if v1 != 0 and num[0] == "0":
                    continue
                if v2 != 0 and num[i] == "0":
                    continue

                k = j
                while k <= len(num):
                    if k == len(num):
                        return True
                    v3 = v1 + v2
                    s3 = str(v3)
                    if num[k:k + len(s3)] == s3:
                        v1, v2 = v2, v3
                        k += len(s3)
                    else:
                        break
        return False
```

