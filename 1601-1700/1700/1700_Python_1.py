from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = [students.count(0), students.count(1)]
        for sandwich in sandwiches:
            if count[sandwich] > 0:
                count[sandwich] -= 1
            else:
                break
        return sum(count)


if __name__ == "__main__":
    # 0
    print(Solution().countStudents(students=[1, 1, 0, 0], sandwiches=[0, 1, 0, 1]))

    # 3
    print(Solution().countStudents(students=[1, 1, 1, 0, 0, 1], sandwiches=[1, 0, 0, 0, 1, 1]))

    # 5
    print(Solution().countStudents(students=[0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
                                   sandwiches=[0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0]))
