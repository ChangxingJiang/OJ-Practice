# LeetCode题解(1108)：IP地址无效化(Python)

题目：[原题链接](https://leetcode-cn.com/problems/defanging-an-ip-address/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | --         | --         | 40ms (63.92%) |
| Ans 2 (Python) | --         | --         | 36ms (84.78%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

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