from typing import List


class Solution:
    # O(NlogN)
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        ans = 0
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        idx = 0
        while truckSize > 0 and idx < len(boxTypes):
            ans += boxTypes[idx][1] * min(boxTypes[idx][0], truckSize)
            truckSize -= boxTypes[idx][0]
            idx += 1

        return ans


if __name__ == "__main__":
    print(Solution().maximumUnits(boxTypes=[[1, 3], [2, 2], [3, 1]], truckSize=4))  # 8
    print(Solution().maximumUnits(boxTypes=[[5, 10], [2, 5], [4, 7], [3, 9]], truckSize=10))  # 91
