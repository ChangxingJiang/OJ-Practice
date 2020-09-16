from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder:
            return True

        root = postorder[-1]
        left_post_order = []
        right_post_order = []
        for n in postorder[:-1]:
            if n < root:
                if not right_post_order:
                    left_post_order.append(n)
                else:
                    return False
            else:
                right_post_order.append(n)

        return self.verifyPostorder(left_post_order) and self.verifyPostorder(right_post_order)


if __name__ == "__main__":
    #      5
    #     / \
    #    2   6
    #   / \
    #  1   3
    print(Solution().verifyPostorder([1, 6, 3, 2, 5]))  # False

    print(Solution().verifyPostorder([1, 3, 2, 6, 5]))  # True

    print(Solution().verifyPostorder([4, 8, 6, 12, 16, 14, 10]))  # True

    print(Solution().verifyPostorder([4, 6, 7, 5]))  # True

    print(Solution().verifyPostorder([5, 4, 3, 2, 1]))  # True

    print(Solution().verifyPostorder([4, 6, 12, 8, 16, 14, 10]))  # False
