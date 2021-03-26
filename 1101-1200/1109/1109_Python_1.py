from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        lst = [0] * (n + 1)
        for j, k, l in bookings:
            lst[j - 1] += l
            lst[k] -= l

        lst.pop()

        ans = []
        now = 0
        for i in range(len(lst)):
            now += lst[i]
            ans.append(now)

        return ans


if __name__ == "__main__":
    # [10,55,45,25,25]
    print(Solution().corpFlightBookings(bookings=[[1, 2, 10], [2, 3, 20], [2, 5, 25]], n=5))
