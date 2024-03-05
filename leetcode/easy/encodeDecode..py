import random
import string
class Codec:
    def __init__(self):
        self.encodeDict = {}
        self.decodeDict = {}
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        baseString = 'http://tinyurl.com/'
        if longUrl not in self.encodeDict.values():
            rString = ''.join(random.choices(string.ascii_lowercase, k=5))
            shortUrl = baseString+rString
            self.encodeDict[shortUrl] = longUrl
        return shortUrl
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.encodeDict[shortUrl]
