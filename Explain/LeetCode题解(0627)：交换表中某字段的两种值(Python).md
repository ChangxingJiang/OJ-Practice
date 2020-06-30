# LeetCode题解(0627)：交换表中某字段的两种值(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/swap-salary/)（简单）

| 解法        | 执行用时       |
| ----------- | -------------- |
| Ans 1 (SQL) | 197ms (34.17%) |
| Ans 2 (SQL) | 192ms (38.34%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（CASE）：

```mysql
UPDATE salary
SET sex = CASE sex WHEN 'f' THEN 'm' ELSE 'f' END;
```

解法二（CASE）：

```mysql
UPDATE salary
SET sex = IF(sex = 'f', 'm', 'f');
```