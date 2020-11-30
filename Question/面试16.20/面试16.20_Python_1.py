from typing import List


class Solution:
    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:
        table = ["2", "2", "2", "3", "3", "3", "4", "4", "4", "5", "5", "5", "6", "6", "6", "7", "7", "7", "7", "8",
                 "8", "8", "9", "9", "9", "9"]

        size = len(num)

        ans = []
        for word in words:
            if len(word) != size:
                continue
            for i in range(len(word)):
                if table[ord(word[i])-97] != num[i]:
                    break
            else:
                ans.append(word)

        return ans


if __name__ == "__main__":
    # ["tree", "used"]
    print(Solution().getValidT9Words(num="8733", words=["tree", "used"]))

    # ["a", "b", "c"]
    print(Solution().getValidT9Words(num="2", words=["a", "b", "c", "d"]))
