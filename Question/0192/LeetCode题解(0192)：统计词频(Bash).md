# LeetCode题解(0192)：统计词频(Bash)

题目：[原题链接](https://leetcode-cn.com/problems/word-frequency/)（中等）

标签：Shell

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时     |
| -------------- | ---------- | ---------- | ------------ |
| Ans 1 (Python) |            |            | 8ms (41.84%) |
| Ans 2 (Python) |            |            |              |
| Ans 3 (Python) |            |            |              |

解法一：

```bash
cat words.txt |tr -s ' ' '\n' |sort|uniq -c|sort -r|awk '{print $2,$1}'
```

