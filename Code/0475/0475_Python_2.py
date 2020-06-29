from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        # print(heaters)
        maximum = 0
        for idx in houses:
            left = 0
            right = len(heaters) - 1
            distance = 0
            while right - left > 1:
                mid = (left + right) // 2
                if heaters[mid] < idx:
                    left = mid
                elif heaters[mid] == idx:
                    break
                else:
                    right = mid
            else:
                distance = min(abs(idx - heaters[left]), abs(heaters[right] - idx))
            # print(idx, distance, heaters[left], heaters[right])
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
