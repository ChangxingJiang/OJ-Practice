import collections
import re
from typing import List


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        # 处理wordlist列表
        word_set = set(wordlist)  # 用于匹配区分大小写的结果

        word_dict = collections.defaultdict(list)  # 用于匹配大小写问题的单词
        vowel_dict = collections.defaultdict(list)  # 用于匹配元音问题的单词
        for word in wordlist:
            lower = word.lower()
            word_dict[lower].append(word)
            vowel_dict[re.sub("[aeiou]", "#", lower)].append(word)

        # 执行匹配
        ans = []
        for query in queries:
            if query in word_set:
                ans.append(query)
            else:
                lower = query.lower()
                if lower in word_dict:
                    ans.append(word_dict[lower][0])
                else:
                    vowel = re.sub("[aeiou]", "#", lower)
                    if vowel in vowel_dict:
                        ans.append(vowel_dict[vowel][0])
                    else:
                        ans.append("")

        return ans


if __name__ == "__main__":
    print(Solution().spellchecker(wordlist=["KiTe", "kite", "hare", "Hare"],
                                  queries=["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet",
                                           "keto"]))  # ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
