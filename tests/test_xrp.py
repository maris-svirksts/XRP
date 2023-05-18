import sys

# Add the project directory to the Python module search path
sys.path.append("..")

from xrpl.wallet import generate_faucet_wallet
from xrpl.clients import JsonRpcClient
from XRP.src.xrp import make_xrp_payment_from_vault

JSON_RPC_URL = "https://s.altnet.rippletest.net:51234/"

def test_make_xrp_payment_from_vault():
    client = JsonRpcClient(JSON_RPC_URL)

    # Create sender wallet.
    sender_wallet = generate_faucet_wallet(client, debug=True)

    # Create receiver wallet.
    receiver_wallet = generate_faucet_wallet(client, debug=True)

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
