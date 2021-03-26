# LeetCode题解(0929)：判断电子邮件地址是否相同(Python)

题目：[原题链接](https://leetcode-cn.com/problems/unique-email-addresses/)（简单）

标签：字符串、正则表达式

| 解法           | 时间复杂度                  | 空间复杂度                  | 执行用时      |
| -------------- | --------------------------- | --------------------------- | ------------- |
| Ans 1 (Python) | --                          | $O(N×K)$ : K为Email平均长度 | 68ms (63.02%) |
| Ans 2 (Python) | $O(N×K)$ : K为Email平均长度 | $O(N×K)$ : K为Email平均长度 | 72ms (48.14%) |
| Ans 3 (Python) |                             |                             |               |

解法一（正则匹配）：

```python
def numUniqueEmails(self, emails: List[str]) -> int:
    hashmap = set()
    for email in emails:
        name, domain = email.split("@")
        total = re.sub("\+.*$", "", name.replace(".", "")) + "@" + domain
        if total not in hashmap:
            hashmap.add(total)
    return len(hashmap)
```

解法二（遍历处理）：

```python
def numUniqueEmails(self, emails: List[str]) -> int:
    hashmap = set()
    for email in emails:
        idx = email.index("@")
        real = ""
        for n in email[:idx]:
            if n == "+":
                break
            elif n != ".":
                real += n
        real += email[idx:]
        if real not in hashmap:
            hashmap.add(real)
    return len(hashmap)
```