from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().countStudents(students=[1, 1, 0, 0], sandwiches=[0, 1, 0, 1]))  # 0
    print(Solution().countStudents(students=[1, 1, 1, 0, 0, 1], sandwiches=[1, 0, 0, 0, 1, 1]))  # 3
