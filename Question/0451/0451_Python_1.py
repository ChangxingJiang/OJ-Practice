import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        count = collections.Counter(s)
        return "".join(sorted(s, key=lambda x: (count[x], x), reverse=True))


if __name__ == "__main__":
    # eert
    print(Solution().frequencySort("tree"))

    # cccaaa
    print(Solution().frequencySort("cccaaa"))

    # bbAa
    print(Solution().frequencySort("Aabb"))
