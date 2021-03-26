# LeetCode题解(0194)：转置文件(Bash)

题目：[原题链接](https://leetcode-cn.com/problems/transpose-file/)（中等）

标签：Shell

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) |            |            | 16ms (32.92%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```bash
line=`cat file.txt|awk '{print NF}'|head -n 1`
for n in $(seq 1 ${line});
do

   cat  file.txt |awk -v n=$n '{print $n}' |xargs echo 

done
```

