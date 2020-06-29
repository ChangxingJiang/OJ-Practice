from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        size = len(heaters)
        maximum = 0
        pos = 0
        for idx in houses:
            while pos < size and heaters[pos] < idx:
                pos += 1
            if pos == 0:
                distance = heaters[0] - idx
            elif pos == size:
                distance = idx - heaters[-1]
            else:
                distance = min(idx - heaters[pos - 1], heaters[pos] - idx)
            if distance > maximum:
                maximum = distance
        return maximum


if __name__ == "__main__":
    print(Solution().findRadius([1, 2, 3], [2]))  # 1
    print(Solution().findRadius([1, 5], [2]))  # 3
    print(Solution().findRadius([1, 2, 3, 4], [1, 4]))  # 1
    print(Solution().findRadius([1, 5], [10]))  # 9
    print(
        Solution().findRadius([282475249, 622650073, 984943658, 144108930, 470211272, 101027544, 457850878, 458777923],
                              [823564440, 115438165, 784484492, 74243042, 114807987, 137522503, 441282327, 16531729,
                               823378840, 143542612]))  # 161834419
