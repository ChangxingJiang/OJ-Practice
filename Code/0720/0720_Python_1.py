from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()

        last_list = []
        now_list = []
        for size in range(1, 31):
            for word in words:
                if len(word) == size and (size == 1 or word[:-1] in last_list):
                    now_list.append(word)
            if len(now_list) == 0:
                break
            last_list = now_list
            now_list = []

        minimum = len(words)
        ans = None
        for word in last_list:
            idx = words.index(word)
            if idx < minimum:
                minimum = idx
                ans = word

        return ans


if __name__ == "__main__":
    print(Solution().longestWord(["w", "wo", "wor", "worl", "world"]))  # world
    print(Solution().longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"]))  # apple
