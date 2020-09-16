from typing import List

from toolkit import TreeNode
from toolkit import build_TreeNode


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


if __name__ == "__main__":
    # [7,4,1]
    tree = build_TreeNode([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    print(Solution().distanceK(tree, tree.left, 2))

    # [3]
    tree = build_TreeNode([0, 1, None, None, 2, None, 3, None, 4])
    print(Solution().distanceK(tree, tree.left, 2))
