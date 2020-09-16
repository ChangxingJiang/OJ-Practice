# LeetCode题解(0193)：使用bash脚本识别有效电话号码(Bash)

题目：[原题链接](https://leetcode-cn.com/problems/valid-phone-numbers/)（简单）

| 解法         | 执行用时    |
| ------------ | ----------- |
| Ans 1 (Bash) | 0ms (>100%) |

解法一：

```bash
grep -P "^(\d{3}-|\(\d{3}\) )\d{3}-\d{4}$" file.txt
```