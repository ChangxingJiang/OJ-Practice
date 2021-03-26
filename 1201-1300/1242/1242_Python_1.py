import collections
import queue
import threading
from typing import List
from urllib.parse import urlsplit


# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
class HtmlParser(object):
    def getUrls(self, url):
        """
        :type url: str
        :rtype List[str]
        """


class Solution:
    def __init__(self):
        self.queue = collections.deque()

    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        domain = urlsplit(startUrl).netloc
        request_queue = queue.Queue()
        result_queue = queue.Queue()
        request_queue.put(startUrl)

        # 启动线程
        for _ in range(5):
            thread = threading.Thread(target=self._run, args=(domain, htmlParser, request_queue, result_queue))
            thread.daemon = True
            thread.start()

        running = 1
        visited = {startUrl}

        while running:
            for url in result_queue.get():
                if url not in visited:
                    visited.add(url)
                    request_queue.put(url)
                    running += 1
            running -= 1

        return list(visited)

    def _run(self, domain, htmlParser, request_queue, result_queue):
        while True:
            now_url = request_queue.get()
            next_url_lst = []
            for next_url in htmlParser.getUrls(now_url):
                if domain == urlsplit(next_url).netloc:
                    next_url_lst.append(next_url)
            result_queue.put(next_url_lst)


if __name__ == "__main__":
    pass
