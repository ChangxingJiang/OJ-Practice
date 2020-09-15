import collections
from typing import List

from toolkit import TreeNode
from toolkit import build_TreeNode


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        ans = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])
        while queue:
            tmp_ans = collections.defaultdict(list)
            for _ in range(len(queue)):
                node, idx = queue.popleft()
                tmp_ans[idx].append(node.val)
                if node.left:
                    queue.append((node.left, idx - 1))
                if node.right:
                    queue.append((node.right, idx + 1))
            for k, v in tmp_ans.items():
                ans[k].extend(sorted(v))

        return [ans[k] for k in sorted(ans.keys())]


if __name__ == "__main__":
    # [[9],[3,15],[20],[7]]
    print(Solution().verticalTraversal(build_TreeNode([3, 9, 20, None, None, 15, 7])))

    # [[4],[2],[1,5,6],[3],[7]]
    print(Solution().verticalTraversal(build_TreeNode([1, 2, 3, 4, 5, 6, 7])))
