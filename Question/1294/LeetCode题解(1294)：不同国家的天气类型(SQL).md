# LeetCode题解(1294)：不同国家的天气类型(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/weather-type-in-each-country/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 395ms (86.60%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT C.country_name,
       T.weather_type
FROM (SELECT country_id,
             CASE
                 WHEN AVG(weather_state) <= 15 THEN 'Cold'
                 WHEN AVG(weather_state) >= 25 THEN 'Hot'
                 ELSE 'Warm' END AS weather_type
      FROM Weather
      WHERE day BETWEEN '2019-11-01' AND '2019-11-30'
      GROUP BY country_id) AS T
         LEFT JOIN
     Countries AS C ON C.country_id = T.country_id;
```