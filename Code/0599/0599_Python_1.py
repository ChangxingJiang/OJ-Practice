from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_mum = float("inf")
        min_name = []
        for i in range(len(list1)):
            n = list1[i]
            if n in list2:
                t = list2.index(n) + i
                if t < min_mum:
                    min_mum = t
                    min_name = [n]
                elif t == min_mum:
                    min_name.append(n)
        return min_name


if __name__ == "__main__":
    # ["Shogun"]
    print(Solution().findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],
                                    ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]))
