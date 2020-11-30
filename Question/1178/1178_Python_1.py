import collections
from typing import List


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        def all_chance(chars):
            lst = [chars[0]]
            chars = list(sorted(set(chars[1:])))
            size = len(chars)
            res = []

            def recursion(i):
                if i == size:
                    res.append("".join(sorted(lst)))
                else:
                    lst.append(chars[i])
                    recursion(i + 1)
                    lst.pop()
                    recursion(i + 1)

            recursion(0)

            return res

        count = collections.Counter()
        for word in words:
            count["".join(sorted(set(word)))] += 1

        ans = []
        for puzzle in puzzles:
            now = 0
            for chance in all_chance(puzzle):
                now += count[chance]
            ans.append(now)

        return ans


if __name__ == "__main__":
    # [1,1,3,2,4,0]
    print(Solution().findNumOfValidWords(words=["aaaa", "asas", "able", "ability", "actt", "actor", "access"],
                                         puzzles=["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"]))

    # [0,1,3,2,0]
    print(Solution().findNumOfValidWords(["apple", "pleas", "please"],
                                         ["aelwxyz", "aelpxyz", "aelpsxy", "saelpxy", "xaelpsy"]))
