from typing import List


class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        if not sentence:
            return 0

        # 构造字典树
        tree = {}
        for word in dictionary:
            node = tree
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node["@"] = None

        size = len(sentence)

        # 计算每个位置开始的所有可能的结尾位置
        maybe = [[] for _ in range(size + 1)]
        for i in range(size):
            j = i
            node = tree
            while j < size and sentence[j] in node:
                node = node[sentence[j]]
                j += 1
                if "@" in node:
                    maybe[i].append(j)

        print([(i, lst) for i, lst in enumerate(maybe)])

        # 计算最小未识别字符数量
        dp = [float("inf") for i in range(size + 1)]

        def track(idx, now):
            # 如果匹配结束则跳过
            if idx == size + 1:
                return

            # 如果当前情况不是最优解，则跳过
            if now >= dp[idx]:
                return

            dp[idx] = now

            # 处理发现单词的各种情况
            for end in maybe[idx]:
                # print(idx, "->", end, "=", now)
                track(end, now)

            # 处理不发现这个位置开始的单词的情况
            track(idx + 1, now + 1)

        track(0, 0)

        # print([(i, d) for i, d in enumerate(dp)])

        return dp[-1]


if __name__ == "__main__":
    # 7
    print(Solution().respace(dictionary=["looked", "just", "like", "her", "brother"],
                             sentence="jesslookedjustliketimherbrother"))

    # 17
    print(Solution().respace(dictionary=["jxnonurhhuanyuqahjy", "phrxu", "hjunypnyhajaaqhxduu"],
                             sentence="qahurhoharrdjxnonurhhuanyuqahjyppnha"))

    # 28
    print(Solution().respace(
        dictionary=["axxpxakkxktpa", "aappk", "kddxxp", "p", "atxtdtpkt", "ptxkatdakp", "padpatxaptpaatkadaxka", "xd",
                    "xa", "kptkaxxpptpkxaxtx", "t", "atdxkttpppakkxkxpxdxxapakaadaxkakapxptdpkxkaadtx", "kp", "xa",
                    "pkkataxkakkxxktxxdptatkkxta", "dxttapxpxkxttkktpkx", "tat", "txpdakdxpaa",
                    "axxkaxkxkkkdpkpttxdkpaaakkakdkkdxatd", "paxaa"],
        sentence="ppkaxpxddkpaatttxtpdtaxtadxaxatxtdtpktdxpppkaxpxddkpaatttxtpdtaxtadx"))
