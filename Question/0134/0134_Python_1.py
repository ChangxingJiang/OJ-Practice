from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        size = len(gas)
        lst = [gas[i] - cost[i] for i in range(size)]

        prefix = []
        min_idx, min_val = -1, float("inf")
        last = 0
        for i in range(size):
            last += lst[i]
            prefix.append(last)
            if last < min_val:
                min_idx, min_val = i, last

        if prefix[-1] < 0:
            return -1
        else:
            return (min_idx + 1) % size


if __name__ == "__main__":
    print(Solution().canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))  # 3
    print(Solution().canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]))  # -1
