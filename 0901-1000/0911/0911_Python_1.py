import bisect
import collections
from typing import List


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.lst = []
        count = collections.Counter()
        max_val, max_num = 0, 0
        for i in range(len(times)):
            count[persons[i]] += 1
            if count[persons[i]] >= max_num:
                max_val, max_num = persons[i], count[persons[i]]
            self.lst.append(max_val)

    def q(self, t: int) -> int:
        idx = bisect.bisect_right(self.times, t) - 1
        return self.lst[idx]


if __name__ == "__main__":
    obj = TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30])
    print(obj.q(3))  # 0
    print(obj.q(12))  # 1
    print(obj.q(25))  # 1
    print(obj.q(15))  # 0
    print(obj.q(24))  # 0
    print(obj.q(8))  # 1
