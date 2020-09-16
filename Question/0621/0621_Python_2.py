import collections
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = collections.Counter(tasks).values()
        total = 0
        max_value = 0
        max_num = 0
        for c in count:
            total += c
            if c > max_value:
                max_value = c
                max_num = 1
            elif c == max_value:
                max_num += 1
        return max((max_value - 1) * (n + 1) + max_num, total)


if __name__ == "__main__":
    print(Solution().leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=2))  # 8
    print(Solution().leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=0))  # 6
    print(Solution().leastInterval(tasks=["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], n=2))  # 16
