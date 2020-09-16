# LeetCode题解(0107)：二叉树的层次遍历(Python)

题目：[题目链接](https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/)（简单）

标签：树、二叉树

| 解法           | 执行用时      |
| :------------- | ------------- |
| Ans 1 (Python) | 40ms (99.73%) |

解法一（广度优先遍历）：

![LeetCode题解(0107)：截图](LeetCode题解(0107)：截图.png)

```python
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        ans = []
        node_list = [root]
        while len(node_list) > 0:
            level_val = []
            temp_node_list = []
            for node in node_list:
                level_val.append(node.val)
                if node.left:
                    temp_node_list.append(node.left)
                if node.right:
                    temp_node_list.append(node.right)
            ans.append(level_val)
            node_list = temp_node_list
        ans.reverse()
        return ans
```