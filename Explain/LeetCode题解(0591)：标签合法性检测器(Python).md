# LeetCode题解(0591)：标签合法性检测器(Python)

题目：[原题链接](https://leetcode-cn.com/problems/tag-validator/)（困难）

标签：字符串、正则表达式

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | --         | --         | 36ms (96.00%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（正则表达式处理）：

```python
def isValid(self, code: str) -> bool:
    # 正则表达式移除CDATA
    code = re.sub(r"<!\[CDATA\[.*\]\]>", "", code)

    # 正则表达式判断是否被一个标签包含
    if not re.match(r"^<([A-Z]{1,9})>.*</\1>$", code, re.S):
        return False

    # 使用正则式移除所有完整标签
    code, num = re.subn(r"<([A-Z]{1,9})>[^<]*</\1>", "", code)
    while num:
        code, num = re.subn(r"<([A-Z]{1,9})>[^<]*</\1>", "", code)
    return not code
```

