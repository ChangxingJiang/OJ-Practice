class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s_map = {}
        g_map = {}
        bulls = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                if secret[i] not in s_map:
                    s_map[secret[i]] = 1
                else:
                    s_map[secret[i]] += 1
                if guess[i] not in g_map:
                    g_map[guess[i]] = 1
                else:
                    g_map[guess[i]] += 1

        cows = 0
        for s in s_map:
            if s in g_map:
                cows += min(s_map[s], g_map[s])

        return str(bulls) + "A" + str(cows) + "B"


if __name__ == "__main__":
    print(Solution().getHint("1807", "7810"))  # 1A3B
    print(Solution().getHint("1123", "0111"))  # 1A1B
