# LeetCode题解(0863)：寻找二叉树中距离指定节点的距离为K的结点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/all-nodes-distance-k-in-binary-tree/)（中等）

标签：树、二叉树、深度优先搜索、广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 48ms (73.28%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（两次遍历）：

```python
class Solution:
    def __init__(self):
        self.ans = []

    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        # 深度优先搜索寻找目标结点
        def dfs(node, distance=-1):
            # 处理当前节点不存在的情况
            if not node:
                return -1

            # 处理当前节点为目标节点子节点的情况
            elif distance >= 0:
                distance += 1
                if distance == K:  # 如果当前节点到目标节点的距离为指定距离，则记录当前节点，不再继续遍历
                    self.ans.append(node.val)
                elif distance < K:  # 如果当前节点到目标节点的距离小于指定距离，则继续遍历当前节点的子节点
                    dfs(node.left, distance)
                    dfs(node.right, distance)
                return distance

            # 处理当前节点即为目标节点的情况
            elif node.val == target.val:
                distance = 0
                if distance == K:  # 如果当前节点到目标节点的距离为指定距离，则记录当前节点，不再继续遍历
                    self.ans.append(node.val)
                elif distance < K:  # 如果当前节点到目标节点的距离小于指定距离，则继续遍历当前节点的子节点
                    dfs(node.left, distance)
                    dfs(node.right, distance)
                return distance

            # 处理目标节点在当前节点的子树中的情况
            else:
                # 递归左子树和右子树
                left_distance = dfs(node.left, distance)
                right_distance = dfs(node.right, distance)

                # 处理目标节点在左子树中的情况
                if left_distance >= 0:
                    distance = left_distance + 1
                    if distance == K:  # 如果当前节点到目标节点的距离为指定距离，则记录当前节点，不再继续遍历
                        self.ans.append(node.val)
                    elif distance < K:  # 如果当前节点到目标节点的距离小于指定距离，则继续遍历右子树
                        dfs(node.right, distance)
                    return distance

                if right_distance >= 0:
                    distance = right_distance + 1
                    if distance == K:  # 如果当前节点到目标节点的距离为指定距离，则记录当前节点，不再继续遍历
                        self.ans.append(node.val)
                    elif distance < K:  # 如果当前节点到目标节点的距离小于指定距离，则继续遍历左子树
                        dfs(node.left, distance)
                    return distance

                return -1

        dfs(root)

        return self.ans
```