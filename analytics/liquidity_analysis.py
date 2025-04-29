import numpy as np

class LiquidityAnalyzer:
    def __init__(self, base_reserve: float, quote_reserve: float):
        self.x = base_reserve
        self.y = quote_reserve
        
    def calculate_price_impact(self, dx: float) -> float:
        k = self.x * self.y
        new_x = self.x + dx
        new_price = k / (new_x ** 2)
        return (new_price - (self.y/self.x)) / (self.y/self.x)
    
    def optimal_arbitrage(self, external_price: float) -> float:
        def profit(dx):
            dy = (self.x * self.y) / (self.x + dx) - self.y
            return dy - dx * external_price
        return max(0, self._solve_newton(profit, 0.1))
    
    def _solve_newton(self, f, x0):
        for _ in range(100):
            fx = f(x0)
            if abs(fx) < 1e-6:
                return x0
            fpx = (f(x0 + 1e-6) - fx) / 1e-6
            x0 -= fx / fpx
        return x0
