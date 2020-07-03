from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0 for _ in range(num_people)]
        num = 1
        idx = 0
        while candies:
            if idx >= num_people:
                idx -= num_people
            if candies >= num:
                ans[idx] += num
                candies -= num
                num += 1
                idx += 1
            else:
                ans[idx] += candies
                break
        return ans


if __name__ == "__main__":
    print(Solution().distributeCandies(candies=7, num_people=4))  # [1,2,3,1]
    print(Solution().distributeCandies(candies=10, num_people=3))  # [5,2,3]
