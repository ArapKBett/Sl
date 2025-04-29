class LiquidityProvider:
    def __init__(self, pool):
        self.pool = pool
        self.lp_tokens = 0
        
    def add_liquidity(self, amount_x: float, amount_y: float):
        if self.pool['x'] == 0 or self.pool['y'] == 0:
            shares = (amount_x * amount_y) ** 0.5
        else:
            shares = min(
                amount_x / self.pool['x'],
                amount_y / self.pool['y']
            ) * self.lp_tokens
        self.pool['x'] += amount_x
        self.pool['y'] += amount_y
        self.lp_tokens += shares
        return shares
    
    def remove_liquidity(self, shares: float):
        x_amount = (shares / self.lp_tokens) * self.pool['x']
        y_amount = (shares / self.lp_tokens) * self.pool['y']
        self.pool['x'] -= x_amount
        self.pool['y'] -= y_amount
        self.lp_tokens -= shares
        return x_amount, y_amount
