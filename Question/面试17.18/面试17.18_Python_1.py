import collections
from typing import List


class Solution:
    def shortestSeq(self, big: List[int], small: List[int]) -> List[int]:
        set_small = set(small)
        s1, s2 = len(big), len(small)
        count = collections.Counter()

        ans_idx, ans_val = [], float("inf")

        now = 0
        left = right = 0
        while right < s1:
            while right < s1 and now < s2:
                if big[right] in set_small:
                    if count[big[right]] == 0:
                        now += 1
                    count[big[right]] += 1
                right += 1

            # print(left, right, count)

            if now == s2:
                while left < right and (big[left] not in set_small or count[big[left]] > 1):
                    if big[left] in set_small:
                        count[big[left]] -= 1
                    left += 1

                if right - left < ans_val:
                    ans_idx, ans_val = [left, right - 1], right - left

                while left < right and now == s2:
                    if big[left] in set_small:
                        count[big[left]] -= 1
                        if count[big[left]] == 0:
                            now -= 1
                    left += 1

        return ans_idx


if __name__ == "__main__":
    # [7,10]
    print(Solution().shortestSeq(big=[7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7], small=[1, 5, 9]))

    # []
    print(Solution().shortestSeq(big=[1, 2, 3], small=[4]))

    # [0,98]
    print(Solution().shortestSeq(
        big=[842, 336, 777, 112, 789, 801, 922, 874, 634, 121, 390, 614, 179, 565, 740, 672, 624, 130, 555, 714, 9, 950,
             887, 375, 312, 862, 304, 121, 360, 579, 937, 148, 614, 885, 836, 842, 505, 187, 210, 536, 763, 880, 652,
             64, 272, 675, 33, 341, 101, 673, 995, 485, 16, 434, 540, 284, 567, 821, 994, 174, 634, 597, 919, 547, 340,
             2, 512, 433, 323, 895, 965, 225, 702, 387, 632, 898, 297, 351, 936, 431, 468, 694, 287, 671, 190, 496, 80,
             110, 491, 365, 504, 681, 672, 825, 277, 138, 778, 851, 732, 176],
        small=[950, 885, 702, 101, 312, 652, 555, 936, 842, 33, 634, 851, 174, 210, 287, 672, 994, 614, 732, 919, 504,
               778, 340, 694, 880, 110, 777, 836, 365, 375, 536, 547, 887, 272, 995, 121, 225, 112, 740, 567, 898, 390,
               579, 505, 351, 937, 825, 323, 874, 138, 512, 671, 297, 179, 277, 304]))
