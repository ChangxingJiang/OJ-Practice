import collections


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        size = len(senate)

        queue1 = collections.deque()
        queue2 = collections.deque()
        for i, ch in enumerate(senate):
            if ch == "R":
                queue1.append(i)
            else:
                queue2.append(i)

        while queue1 and queue2:
            if queue1[0] < queue2[0]:
                queue1.append(queue1.popleft() + size)
                queue2.popleft()
            else:
                queue2.append(queue2.popleft() + size)
                queue1.popleft()

        return "Radiant" if queue1 else "Dire"


if __name__ == "__main__":
    print(Solution().predictPartyVictory("RD"))  # "Radiant"
    print(Solution().predictPartyVictory("RDD"))  # "Dire"
