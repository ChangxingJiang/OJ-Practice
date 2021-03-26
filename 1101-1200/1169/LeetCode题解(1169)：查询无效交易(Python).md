# LeetCode题解(1169)：依据指定条件查询无效交易(Python)

题目：[原题链接](https://leetcode-cn.com/problems/invalid-transactions/)（中等）

标签：字符串、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 116ms (53.00%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（哈希表）：

```python
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # 依据人名重新分组交易记录
        # 时间复杂度：O(N)
        transactions_by_name = collections.defaultdict(list)
        for transaction in transactions:
            name, time, money, city = transaction.split(",")
            transactions_by_name[name].append((int(time), city, int(money)))

        ans = set()

        # 依据各组人名分别排序并检查记录
        for name, transactions in transactions_by_name.items():
            transactions.sort()
            for i in range(len(transactions)):
                time1, city1, money1 = transactions[i]
                if money1 > 1000:
                    ans.add(",".join([name, str(time1), str(money1), city1]))
                for j in range(i + 1, len(transactions)):
                    time2, city2, money2 = transactions[j]
                    if time2 - time1 > 60:
                        break
                    if city1 != city2:
                        ans.add(",".join([name, str(time1), str(money1), city1]))
                        ans.add(",".join([name, str(time2), str(money2), city2]))

        return list(ans)
```