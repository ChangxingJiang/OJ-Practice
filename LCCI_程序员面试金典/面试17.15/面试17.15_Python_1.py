from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        word_set = set(words)

        # 构造字典树
        tree = {}
        for word in words:
            node = tree
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node["@"] = None

        # 判断是否由其他单词组成
        def is_consist(s, split=False):
            if split and s in word_set:
                return True

            n = tree
            for i, c in enumerate(s):
                if "@" in n and is_consist(s[i:], split=True):
                    return True
                if c in n:
                    n = n[c]
                else:
                    return False

            return False

        ans = sorted([word for word in words if is_consist(word)], key=lambda x: (-len(x), x))

        return ans[0] if ans else ""


if __name__ == "__main__":
    # dogwalker
    print(Solution().longestWord(["cat", "banana", "dog", "nana", "walk", "walker", "dogwalker"]))

    # ccc
    print(Solution().longestWord(["llllcccl", "clclll", "ccc", "llccllccl", "lcclccclcl", "c"]))

    # mmmmhm
    print(Solution().longestWord(["hh", "mmmmhm", "wmmh", "mmhmhmhwm", "h", "hhmh", "mmwwh", "hhwmwm", "m", "mwhhwwm"]))
