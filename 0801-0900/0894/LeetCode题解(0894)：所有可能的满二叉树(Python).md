# LeetCode题解(0894)：计算包含指定节点数量的所有可能的满二叉树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/all-possible-full-binary-trees/)（中等）

标签：树、二叉树、递归

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N!)$    | $O(N!)$    | 超出时间限制   |
| Ans 2 (Python) | $O(2^N)$   | $O(2^N)$   | 236ms (69.88%) |
| Ans 3 (Python) |            |            |                |

解法一（暴力递归）：

```python
class Solution:
    def __init__(self):
        self.ans = []
        self.already = set()

    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        # 处理无法实现满二叉树的情况
        if N % 2 == 0:
            return []

        # 计算需要递归的深度
        n = N // 2

        # 递归生成所有满足的结果
        root = TreeNode(0)

        def recursor(leaf_lst, k):
            if k == 0:
                if (tree_str := str(root)) not in self.already:
                    self.ans.append(copy.deepcopy(root))
                    self.already.add(tree_str)
            else:
                for leaf in leaf_lst:
                    leaf.left = TreeNode(0)
                    leaf.right = TreeNode(0)
                    new_leaf_lst = leaf_lst.copy()
                    new_leaf_lst.remove(leaf)
                    new_leaf_lst.append(leaf.left)
                    new_leaf_lst.append(leaf.right)
                    recursor(new_leaf_lst, k - 1)
                    leaf.right = None
                    leaf.left = None

        recursor([root], n)

        return self.ans
```

解法二（记录每个节点数量的满二叉树的情况）：

```python
class Solution:
    def __init__(self):
        self.memo = {
            0: [],
            1: [TreeNode(0)]
        }

    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N % 2 == 0:
            return []
        if N not in self.memo:
            ans = []
            for left in range(1, N, 2):
                right = N - left - 1
                for left_tree in self.allPossibleFBT(left):
                    for right_tree in self.allPossibleFBT(right):
                        root = TreeNode(0)
                        root.left = left_tree
                        root.right = right_tree
                        ans.append(root)
            self.memo[N] = ans

        return self.memo[N]
```



