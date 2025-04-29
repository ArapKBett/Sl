from cmd import Cmd
import hashlib
from auth.wallet_manager import HdWalletManager
from automations.deployer import TokenDeployer, TokenParameters

class PumpManagerShell(Cmd):
    prompt = 'pump-manager> '
    
    def __init__(self):
        super().__init__()
        self.wallet = HdWalletManager(
            seed=hashlib.sha256(b'proper-seed-for-simulation').digest()
        )
        self.account = self.wallet.derive_account("m/44'/60'/0'/0/0")
        self.deployer = TokenDeployer(self.account)
        
    def do_deploy(self, args):
        """Deploy new token: deploy <name> <symbol> <supply>"""
        try:
            name, symbol, supply = args.split()
            params = TokenParameters(
                name=name,
                symbol=symbol,
                supply=float(supply),
                decimals=9
            )
            result = self.deployer.deploy(params)
            print(f"Deployed {symbol} at {result['contract_address']}")
        except Exception as e:
            print(f"Error: {str(e)}")

    def do_wallet(self, _):
        """Show wallet information"""
        print("Wallet Details:")
        print(f"- Address: {self.account['address']}")
        print(f"- Path: {self.account['path']}")
        print(f"- Public Key: {self.account['public_key'][:20]}...")

    def do_exit(self, _):
        """Exit the application"""
        print("Exiting simulated environment")
        return True

if __name__ == "__main__":
    PumpManagerShell().cmdloop()
    print("\nDISCLAIMER: Educational use only")
