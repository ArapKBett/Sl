class AMMRouter:
    def __init__(self, pool):
        self.pool = pool
        
    def swap_exact_input(self, amount_in: float, token_in: str):
        if token_in == 'base':
            output = (self.pool['y'] * amount_in) / (self.pool['x'] + amount_in)
            self.pool['x'] += amount_in
            self.pool['y'] -= output
        else:
            output = (self.pool['x'] * amount_in) / (self.pool['y'] + amount_in)
            self.pool['y'] += amount_in
            self.pool['x'] -= output
        return output * 0.997
    
    def calculate_slippage(self, amount_in: float) -> float:
        k = self.pool['x'] * self.pool['y']
        new_x = self.pool['x'] + amount_in
        new_price = k / (new_x ** 2)
        return (new_price - (self.pool['y']/self.pool['x'])) / (self.pool['y']/self.pool['x'])
