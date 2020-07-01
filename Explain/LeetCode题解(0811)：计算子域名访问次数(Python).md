# LeetCode题解(0811)：计算子域名访问次数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/subdomain-visit-count/)（简单）

| 解法           | 时间复杂度                       | 空间复杂度 | 执行用时      |
| -------------- | -------------------------------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N×k)$ : k为平均包含子域名数量 | $O(N)$     | 64ms (84.25%) |
| Ans 2 (Python) |                                  |            |               |
| Ans 3 (Python) |                                  |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（哈希表）：

```python
def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
    hashmap = {}
    for cpdomain in cpdomains:
        cp_split = cpdomain.split(" ")
        num = int(cp_split[0])
        domain = cp_split[1]
        while len(domain) > 0:
            if domain not in hashmap:
                hashmap[domain] = num
            else:
                hashmap[domain] += num
            if "." not in domain:
                break
            else:
                domain = domain[domain.index(".") + 1:]

    ans = []
    for key, value in hashmap.items():
        ans.append(str(value) + " " + key)
    return ans
```