from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        pass


if __name__ == "__main__":
    # [['B', '1', 'E', '1', 'B'],
    #  ['B', '1', 'M', '1', 'B'],
    #  ['B', '1', '1', '1', 'B'],
    #  ['B', 'B', 'B', 'B', 'B']]
    print(Solution().updateBoard([
        ['E', 'E', 'E', 'E', 'E'],
        ['E', 'E', 'M', 'E', 'E'],
        ['E', 'E', 'E', 'E', 'E'],
        ['E', 'E', 'E', 'E', 'E']
    ], [3, 0]))

    # [['B', '1', 'E', '1', 'B'],
    #  ['B', '1', 'X', '1', 'B'],
    #  ['B', '1', '1', '1', 'B'],
    #  ['B', 'B', 'B', 'B', 'B']]
    print(Solution().updateBoard([
        ['B', '1', 'E', '1', 'B'],
        ['B', '1', 'M', '1', 'B'],
        ['B', '1', '1', '1', 'B'],
        ['B', 'B', 'B', 'B', 'B']
    ], [1, 2]))
