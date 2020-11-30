from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))

        ans = 1
        count = {}
        for word in words:
            size = len(word)
            if size == 1:
                count[word] = 1
            else:
                min_from = float("inf")
                for i in range(size):
                    sorted_word = "".join(sorted(word[:i] + word[i + 1:]))
                    if sorted_word in count:
                        min_from = min(min_from, count[sorted_word])

                if min_from != float("inf"):
                    ans = max(ans, size - min_from + 1)
                    count["".join(sorted(word))] = min_from
                else:
                    count["".join(sorted(word))] = size

        return ans


if __name__ == "__main__":
    # 4
    print(Solution().longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"]))

    # 7
    print(Solution().longestStrChain(
        ["ksqvsyq", "ks", "kss", "czvh", "zczpzvdhx", "zczpzvh", "zczpzvhx", "zcpzvh", "zczvh", "gr", "grukmj",
         "ksqvsq", "gruj", "kssq", "ksqsq", "grukkmj", "grukj", "zczpzfvdhx", "gru"]))
