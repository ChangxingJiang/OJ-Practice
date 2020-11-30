from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().canAttendMeetings(intervals=[[0, 30], [5, 10], [15, 20]]))  # False
    print(Solution().canAttendMeetings(intervals=[[7, 10], [2, 4]]))  # True
