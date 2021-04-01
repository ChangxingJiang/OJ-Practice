from typing import List


class Solution:
    def canEat(self, candies_count: List[int], queries: List[List[int]]) -> List[bool]:
        prefix_candies_count = [0]
        for num in candies_count:
            prefix_candies_count.append(prefix_candies_count[-1] + num)

        ans = []
        for favorite_type, favorite_day, daily_cap in queries:
            min_num = prefix_candies_count[favorite_type] - daily_cap + 1  # 这一天之前吃的最少数量
            max_num = prefix_candies_count[favorite_type] + candies_count[favorite_type] - 1  # 这一天吃的最多数量

            min_eat = 1 * favorite_day
            max_eat = daily_cap * favorite_day

            ans.append(min_num <= min_eat <= max_num or
                       min_num <= max_eat <= max_num or
                       min_eat <= min_num <= max_num <= max_eat)

        return ans


if __name__ == "__main__":
    # [true,false,true]
    print(Solution().canEat(candies_count=[7, 4, 5, 3, 8], queries=[[0, 2, 2], [4, 2, 4], [2, 13, 1000000000]]))

    # [false,true,true,false,false]
    print(Solution().canEat(candies_count=[5, 2, 6, 4, 1],
                            queries=[[3, 1, 2], [4, 10, 3], [3, 10, 100], [4, 100, 30], [1, 3, 1]]))
