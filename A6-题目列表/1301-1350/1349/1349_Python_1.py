from typing import List


class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        pass


if __name__ == "__main__":
    # 4
    print(Solution().maxStudents(seats=[["#", ".", "#", "#", ".", "#"],
                                        [".", "#", "#", "#", "#", "."],
                                        ["#", ".", "#", "#", ".", "#"]]))

    # 3
    print(Solution().maxStudents(seats=[[".", "#"],
                                        ["#", "#"],
                                        ["#", "."],
                                        ["#", "#"],
                                        [".", "#"]]))

    # 10
    print(Solution().maxStudents(seats=[["#", ".", ".", ".", "#"],
                                        [".", "#", ".", "#", "."],
                                        [".", ".", "#", ".", "."],
                                        [".", "#", ".", "#", "."],
                                        ["#", ".", ".", ".", "#"]]))
