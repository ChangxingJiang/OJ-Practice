from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().validateBinaryTreeNodes(n=4, leftChild=[1, -1, 3, -1], rightChild=[2, -1, -1, -1]))  # True
    print(Solution().validateBinaryTreeNodes(n=4, leftChild=[1, -1, 3, -1], rightChild=[2, 3, -1, -1]))  # False
    print(Solution().validateBinaryTreeNodes(n=2, leftChild=[1, 0], rightChild=[-1, -1]))  # False
    print(Solution().validateBinaryTreeNodes(n=6, leftChild=[1, -1, -1, 4, -1, -1],
                                             rightChild=[2, -1, -1, 5, -1, -1]))  # False
