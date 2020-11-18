from typing import List


class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        pass


if __name__ == "__main__":
    #      |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
    # AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
    #                   | 0 0 1 |

    print(Solution().multiply(
        A=[
            [1, 0, 0],
            [-1, 0, 3]
        ], B=[
            [7, 0, 0],
            [0, 0, 0],
            [0, 0, 1]
        ]))
