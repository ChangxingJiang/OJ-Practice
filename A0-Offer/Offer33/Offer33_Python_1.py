from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        pass


if __name__ == "__main__":
    #      5
    #     / \
    #    2   6
    #   / \
    #  1   3
    print(Solution().verifyPostorder([1, 6, 3, 2, 5]))  # False

    print(Solution().verifyPostorder([1, 3, 2, 6, 5]))  # True
