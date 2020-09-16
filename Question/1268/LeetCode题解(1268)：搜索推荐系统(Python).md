# LeetCode题解(1268)：基于输入前缀的搜索推荐系统(Python)

题目：[原题链接](https://leetcode-cn.com/problems/search-suggestions-system/)（中等）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 104ms (76.87%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

> 因为只搜索一个词，所以没必要建字典树中其他用不到的部分。

```python
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        ans = []
        now_products = products
        for i, ch in enumerate(searchWord):
            new_products = []
            for product in now_products:
                if i < len(product) and product[i] == ch:
                    new_products.append(product)
            ans.append(new_products[:3])
            now_products = new_products
        return ans
```