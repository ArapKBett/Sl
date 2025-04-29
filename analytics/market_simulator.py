import numpy as np

class OrderBookSimulator:
    def __init__(self, base_price: float):
        self.bids = []
        self.asks = []
        self.spread = 0.01  # 1%
        
    def generate_orders(self, volatility: float, n_orders=100):
        prices = np.random.normal(
            loc=base_price, 
            scale=base_price*volatility,
            size=n_orders
        )
        self.bids = sorted(prices * (1 - self.spread/2), reverse=True)
        self.asks = sorted(prices * (1 + self.spread/2))
        
    def match_orders(self, price: float) -> float:
        executed = 0
        while self.bids and self.bids[0] >= price:
            executed += self.bids.pop(0)
        while self.asks and self.asks[0] <= price:
            executed += self.asks.pop(0)
        return executed
