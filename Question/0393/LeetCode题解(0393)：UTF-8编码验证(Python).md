# LeetCode题解(0393)：UTF-8编码验证(Python)

题目：[原题链接](https://leetcode-cn.com/problems/utf-8-validation/)（中等）

标签：位运算

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 156ms (20.41%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def validUtf8(self, data: List[int], idx=0) -> bool:
        # 处理到达末尾的情况
        if idx == len(data):
            return True

        # 处理单字节的情况
        if data[idx] & (1 << 7) == 0:
            return self.validUtf8(data, idx + 1)

        # 处理10xxxxxx的错误情况
        if data[idx] & (1 << 6) == 0:
            return False

        # 处理n字节的情况
        for i in range(5, 2, -1):
            if data[idx] & (1 << i) == 0:
                length = 7 - i  # 计算UTF-8字节数
                if len(data) < idx + length:
                    return False
                for j in range(idx + 1, idx + length):
                    if data[j] & (1 << 7) == 0 or data[j] & (1 << 6) != 0:
                        return False
                return self.validUtf8(data, idx + length)

        return False
```

