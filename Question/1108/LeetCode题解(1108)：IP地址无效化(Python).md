# LeetCode题解(1108)：IP地址无效化(Python)

题目：[原题链接](https://leetcode-cn.com/problems/defanging-an-ip-address/)（简单）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 40ms (63.92%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 36ms (84.78%) |
| Ans 3 (Python) |            |            |               |

解法一（替换函数）：

```python
def defangIPaddr(self, address: str) -> str:
    return address.replace(".", "[.]")
```

解法二（拆分字符串）：

```
def defangIPaddr(self, address: str) -> str:
    return "[.]".join(address.split("."))
```