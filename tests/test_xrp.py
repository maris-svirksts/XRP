from xrpl.wallet import Wallet
from xrpl.clients import Client
from ..src.xrp import make_xrp_payment_from_vault

def test_make_xrp_payment_from_vault():
    # Create sender wallet
    sender_wallet = Wallet.create(test=True)

    # Create receiver wallet
    receiver_wallet = Wallet.create(test=True)

    vault_url = "https://vault.example.com"
    vault_token = "my-token"
    vault_path = "path/to/secret/key"
    sender_wallet_address = sender_wallet.classic_address
    receiver_wallet_address = receiver_wallet.classic_address
    amount = "1"

    response = make_xrp_payment_from_vault(
        vault_url,
        vault_token,
        vault_path,
        sender_wallet_address,
        receiver_wallet_address,
        amount
    )

    assert 'tx_json' in response
