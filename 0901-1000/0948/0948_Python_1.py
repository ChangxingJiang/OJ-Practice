import collections
from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        tokens = collections.deque(tokens)

        mark = 0
        while tokens:
            # 第一次补充积分
            if not mark:
                if power > tokens[0]:
                    power -= tokens.popleft()
                    mark += 1
                    continue
                else:
                    break

            # 补充能量
            if power < tokens[0]:
                if len(tokens) > 1:
                    power += tokens.pop()
                    mark -= 1
                else:
                    break

            else:
                power -= tokens.popleft()
                mark += 1

        return mark


if __name__ == "__main__":
    print(Solution().bagOfTokensScore(tokens=[100], power=50))  # 0
    print(Solution().bagOfTokensScore(tokens=[100, 200], power=150))  # 1
    print(Solution().bagOfTokensScore(tokens=[100, 200, 300, 400], power=200))  # 2
