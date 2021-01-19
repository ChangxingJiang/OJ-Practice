import collections
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        size = len(deck)
        deck.sort()

        index = collections.deque(range(size))
        ans = [0] * size

        for card in sorted(deck):
            ans[index.popleft()] = card
            if index:
                index.append(index.popleft())

        return ans


if __name__ == "__main__":
    # [2,13,3,11,5,17,7]
    print(Solution().deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7]))
