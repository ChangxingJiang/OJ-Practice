from typing import List


class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().deleteTreeNodes(nodes=7, parent=[-1, 0, 0, 1, 2, 2, 2], value=[1, -2, 4, 0, -2, -1, -1]))  # 2
    print(Solution().deleteTreeNodes(nodes=7, parent=[-1, 0, 0, 1, 2, 2, 2], value=[1, -2, 4, 0, -2, -1, -2]))  # 6
    print(Solution().deleteTreeNodes(nodes=5, parent=[-1, 0, 1, 0, 0], value=[-672, 441, 18, 728, 378]))  # 5
    print(Solution().deleteTreeNodes(nodes=5, parent=[-1, 0, 0, 1, 1], value=[-686, -842, 616, -739, -746]))  # 5
