from typing import List


class Solution:
    def findString(self, words: List[str], s: str) -> int:
        left, right = 0, len(words) - 1
        while left <= right:
            mid = (left + right) // 2

            while mid <= right and words[mid] == "":
                mid += 1

            if mid > right:
                right = (left + right) // 2 - 1

            elif words[mid] < s:
                left = mid + 1
            elif words[mid] > s:
                right = mid - 1
            else:
                return mid
        return -1


if __name__ == "__main__":
    # -1
    print(Solution().findString(words=["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""], s="ta"))

    # 4
    print(Solution().findString(words=["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""], s="ball"))

    # 4
    print(Solution().findString(
        words=["DirNnILhARNS hOYIFB", "SM ", "YSPBaovrZBS", "evMMBOf", "mCrS", "oRJfjw gwuo", "xOpSEXvfI"], s="mCrS"
    ))
