from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        # 寻找需要删除的节点
        def find(last_node, now_node):
            if not now_node:
                return None, None
            elif key == now_node.val:
                return last_node, now_node
            elif key < now_node.val:
                return find(now_node, now_node.left)
            elif key > now_node.val:
                return find(now_node, now_node.right)

        delete_node_father, delete_node = find(None, root)

        # 处理没有找到需要删除的节点的情况
        if not delete_node:
            return root

        left_branch = delete_node.left
        right_branch = delete_node.right

        # 执行删除操作
        if left_branch and right_branch:  # 处理两侧分支都存在的情况
            new_node = node = right_branch
            while node.left:
                node = node.left
            node.left = left_branch
        elif left_branch or right_branch:
            new_node = left_branch or right_branch
        else:
            new_node = None

        if not delete_node_father:
            return new_node
        elif delete_node_father.left and delete_node_father.left.val == key:
            delete_node_father.left = new_node
            return root
        else:
            delete_node_father.right = new_node
            return root


if __name__ == "__main__":
    # [5,4,6,2,None,None,7]
    print(Solution().deleteNode(build_TreeNode([5, 3, 6, 2, 4, None, 7]), 3))

    # [5, 3, 6, 2, 4, None, 7]
    print(Solution().deleteNode(build_TreeNode([5, 3, 6, 2, 4, None, 7]), 0))

    print(Solution().deleteNode(build_TreeNode([5, 3, 6, 2, 4, None, 7]), 7))
