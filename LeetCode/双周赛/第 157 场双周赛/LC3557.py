from collections import defaultdict


class Solution:
    def maxSubstrings(self, word: str) -> int:
        char_hash = defaultdict(list)
        result = 0
        for i, ch in enumerate(word):
            char_list = char_hash[ch]
            j = len(char_list) - 1
            while j >= 0 and char_list[j] > i - 3:
                j -= 1
            if j >= 0:
                result += 1
                char_hash = defaultdict(list)
            else:
                char_hash[ch].append(i)
        return result


if __name__ == "__main__":
    print(Solution().maxSubstrings("abcdeafdef"))  # 2
    print(Solution().maxSubstrings("bcdaaaab"))  # 1
