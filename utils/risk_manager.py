class RiskValidator:
    @staticmethod
    def validate_tx(tx: dict) -> bool:
        checks = [
            tx['value'] <= settings.RISK_PARAMS['max_position_size'],
            tx['slippage'] <= settings.RISK_PARAMS['max_slippage'],
            tx['gas'] * tx['gas_price'] < settings.SIMULATION_PARAMS['initial_balance']
        ]
        return all(checks)
    
    @staticmethod
    def portfolio_risk(holdings: dict) -> float:
        total = sum(holdings.values())
        return max(holdings.values()) / total if total > 0 else 0
