from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x), reverse=True)

        ans = 0

        lst = set()
        for word in words:
            if word not in lst:
                ans += len(word) + 1
            for i in range(len(word)):
                lst.add(word[i:])

        return ans


if __name__ == "__main__":
    print(Solution().minimumLengthEncoding(words=["time", "me", "bell"]))  # 10
