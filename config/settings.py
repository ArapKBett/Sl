from enum import Enum

class Network(Enum):
    MAINNET = 1
    TESTNET = 2
    SIMULATION = 3

CURRENT_NETWORK = Network.SIMULATION

SIMULATION_PARAMS = {
    'max_tx_per_second': 5,
    'initial_balance': 100.0,
    'gas_price': 0.001
}

RISK_PARAMS = {
    'max_slippage': 2.0,
    'max_position_size': 0.1
}
