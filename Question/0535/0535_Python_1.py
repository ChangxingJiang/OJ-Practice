class Codec:

    def __init__(self):
        self.hashmap = {}

    def encode(self, longUrl: str) -> str:
        token = str(hash(longUrl))
        self.hashmap[token] = longUrl
        return str(token)

    def decode(self, shortUrl: str) -> str:
        if shortUrl in self.hashmap:
            val = self.hashmap[shortUrl]
            del self.hashmap[shortUrl]
            return val


if __name__ == "__main__":
    obj = Codec()
    print(obj.decode(obj.encode("https://leetcode.com/problems/design-tinyurl")))
