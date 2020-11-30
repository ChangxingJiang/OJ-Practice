# LeetCode题解(1418)：点菜展示表(Python)

题目：[原题链接](https://leetcode-cn.com/problems/display-table-of-food-orders-in-a-restaurant/)（中等）

标签：哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 100ms (79.17%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（两次遍历）：

```python
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        food_set = set()
        for order in orders:
            if order[2] not in food_set:
                food_set.add(order[2])

        food_lst = list(sorted(food_set))
        food_num = len(food_lst)
        food_dic = {food: i for i, food in enumerate(food_lst)}

        table_dic = {}
        for order in orders:
            table, food = int(order[1]), order[2]
            if table not in table_dic:
                table_dic[table] = [0] * food_num
            table_dic[table][food_dic[food]] += 1

        result = [["Table"] + food_lst]
        for table in sorted(table_dic.keys()):
            result.append([str(table)] + [str(n) for n in table_dic[table]])

        return result
```