import collections
from typing import List


class Solution:
    _CHANGE_LIST = {
        "A": ["C", "G", "T"],
        "C": ["A", "G", "T"],
        "G": ["A", "C", "T"],
        "T": ["A", "C", "G"]
    }

    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if start == end:
            return 0

        bank = set(bank)

        def get_change(s1):
            for i, ch1 in enumerate(s1):
                for ch2 in self._CHANGE_LIST[ch1]:
                    s2 = s1[:i] + ch2 + s1[i + 1:]
                    if s2 in bank:
                        yield s2

        visited = set()
        queue = collections.deque([start])
        ans = 0
        while queue:
            ans += 1
            for _ in range(len(queue)):
                now = queue.popleft()
                for change in get_change(now):
                    if change == end:
                        return ans
                    if change not in visited:
                        visited.add(change)
                        queue.append(change)

        return -1


if __name__ == "__main__":
    # 1
    print(Solution().minMutation(start="AACCGGTT",
                                 end="AACCGGTA",
                                 bank=["AACCGGTA"]))

    # 2
    print(Solution().minMutation(start="AACCGGTT",
                                 end="AAACGGTA",
                                 bank=["AACCGGTA", "AACCGCTA", "AAACGGTA"]))

    # 3
    print(Solution().minMutation(start="AAAAACCC",
                                 end="AACCCCCC",
                                 bank=["AAAACCCC", "AAACCCCC", "AACCCCCC"]))

    # -1
    print(Solution().minMutation(start="AAAAAAAA",
                                 end="CCCCCCCC",
                                 bank=["AAAAAAAA", "AAAAAAAC", "AAAAAACC", "AAAAACCC", "AAAACCCC", "AACACCCC",
                                       "ACCACCCC", "ACCCCCCC", "CCCCCCCA"]))
