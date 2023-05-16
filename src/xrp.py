from xrpl.wallet import Wallet
from xrpl.clients import Client
from .vault import load_secret_key_from_vault

def make_xrp_payment(wallet_address: str, secret_key: str, destination_address: str, amount: str) -> dict:
    wallet = Wallet(seed=secret_key)
    client = Client(testnet=True)
    response = client.submit_transaction(wallet.send_xrp(
        amount=amount,
        destination=destination_address,
        fee=None,
        sequence=client.get_account_info(wallet.classic_address)['sequence'],
    ))
    return response

def make_xrp_payment_from_vault(vault_url: str, vault_token: str, vault_path: str, wallet_address: str, destination_address: str, amount: str) -> dict:
    secret_key = load_secret_key_from_vault(vault_url, vault_token, vault_path)
    response = make_xrp_payment(wallet_address, secret_key, destination_address, amount)
    return response
