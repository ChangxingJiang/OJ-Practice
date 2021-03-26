from typing import List


class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        dic = {0: 0}
        count = 0
        ans_idx, ans_val = (0, 0), 0
        for i in range(len(array)):
            if array[i].isnumeric():
                count += 1
            else:
                count -= 1

            if count in dic:
                l, r = dic[count], i + 1
                if r - l + 1 > ans_val:
                    ans_idx, ans_val = (l, r), r - l + 1
            else:
                dic[count] = i + 1

            # print(i, count, ans_idx, ans_val, dic)

        return array[ans_idx[0]:ans_idx[1]]


if __name__ == "__main__":
    # ["A","1","B","C","D","2","3","4","E","5","F","G","6","7"]
    print(Solution().findLongestSubarray(
        ["A", "1", "B", "C", "D", "2", "3", "4", "E", "5", "F", "G", "6", "7", "H", "I", "J", "K", "L", "M"]))

    # []
    print(Solution().findLongestSubarray(["A", "A"]))

    # ["A","1"]
    print(Solution().findLongestSubarray(["A", "1"]))
