import requests
import time

class RateLimitedClient:
    def __init__(self, rps=5):
        self.rps = rps
        self.last_request = 0
        
    def get(self, url):
        elapsed = time.time() - self.last_request
        if elapsed < 1/self.rps:
            time.sleep(1/self.rps - elapsed)
        self.last_request = time.time()
        return requests.get(url)
    
    def post(self, url, data):
        elapsed = time.time() - self.last_request
        if elapsed < 1/self.rps:
            time.sleep(1/self.rps - elapsed)
        self.last_request = time.time()
        return requests.post(url, data)
