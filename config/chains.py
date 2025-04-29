class ChainPresets:
    SOLANA = {
        'decimals': 9,
        'tx_size_limit': 1232,
        'program_id': 'TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA'
    }
    
    ETHEREUM = {
        'decimals': 18,
        'tx_size_limit': 128 * 1024,
        'contract_size_limit': 24576
    }
    
    @staticmethod
    def get_chain_config(network: str):
        return {
            'solana': ChainPresets.SOLANA,
            'ethereum': ChainPresets.ETHEREUM
        }.get(network.lower())
