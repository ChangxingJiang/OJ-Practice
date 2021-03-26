# LeetCode题解(1364)：顾客的可信联系人数量(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-trusted-contacts-of-a-customer/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) |            |            | 1162ms (11.60%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```mysql
SELECT I.invoice_id,
       C.customer_name,
       I.price,
       IFNULL(U1.contacts_cnt, 0) AS contacts_cnt,
       IFNULL(U2.trusted_contacts_cnt, 0) AS trusted_contacts_cnt
FROM Invoices AS I
         LEFT JOIN
     Customers AS C ON I.user_id = C.customer_id
         LEFT JOIN
     (SELECT user_id,
             contact_name AS customer_name,
             COUNT(contact_name) AS contacts_cnt
      FROM Contacts
      GROUP BY user_id) AS U1 ON I.user_id = U1.user_id
         LEFT JOIN
     (SELECT user_id,
             COUNT(contact_name) AS trusted_contacts_cnt
      FROM Contacts
      WHERE contact_email IN (SELECT email FROM Customers)
      GROUP BY user_id) AS U2 ON I.user_id = U2.user_id
ORDER BY I.invoice_id;
```