import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import StandardScaler

class MarketPatternClassifier:
    def __init__(self):
        self.model = GradientBoostingClassifier()
        self.scaler = StandardScaler()
        self.classes = ['normal', 'pump', 'dump']
        
    def train(self, X: np.ndarray, y: np.ndarray):
        X_scaled = self.scaler.fit_transform(X)
        self.model.fit(X_scaled, y)
        
    def predict(self, features: list) -> str:
        scaled = self.scaler.transform([features])
        return self.classes[self.model.predict(scaled)[0]]
    
    def feature_extractor(self, market_data: dict) -> list:
        return [
            market_data['price_change_5m'],
            market_data['volume_change_15m'],
            market_data['liquidity_ratio'],
            market_data['social_mentions']
        ]
