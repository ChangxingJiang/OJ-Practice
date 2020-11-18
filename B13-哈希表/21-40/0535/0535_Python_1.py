class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """


if __name__ == "__main__":
    obj = Codec()
    print(obj.decode(obj.encode("https://leetcode.com/problems/design-tinyurl")))
