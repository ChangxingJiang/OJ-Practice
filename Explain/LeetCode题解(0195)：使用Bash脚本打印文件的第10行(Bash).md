# LeetCode题解(0195)：使用Bash脚本打印文件的第10行(Bash)

题目：[原题链接](https://leetcode-cn.com/problems/tenth-line/)（简单）

| 解法         | 执行用时      |
| ------------ | ------------- |
| Ans 1 (Bash) | 4ms (>80.09%) |

解法一：

```bash
awk "NR==10" file.txt
```

