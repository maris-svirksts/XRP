# Define the network client
# Live: https://s2.ripple.com:51234/
# Test: https://s.altnet.rippletest.net:51234/

def create_client():
    from xrpl.clients import JsonRpcClient
    JSON_RPC_URL = "https://s.altnet.rippletest.net:51234/"
    return JsonRpcClient(JSON_RPC_URL)

# Create a wallet using the testnet faucet:
# https://xrpl.org/xrp-testnet-faucet.html
def create_account(client):
    from xrpl.wallet import generate_faucet_wallet
    wallet = generate_faucet_wallet(client, debug=True)

    return wallet

# Derive an x-address from the classic address:
# https://xrpaddress.info/
def print_addresses(wallet):
    from xrpl.core import addresscodec
    test_xaddress = addresscodec.classic_address_to_xaddress(wallet.classic_address, tag=12345, is_test_network=True)
    print("\nClassic address:\n\n", wallet.classic_address)
    print("X-address:\n\n", test_xaddress)

# Look up info about your account
def print_account_info(client, wallet):
    from xrpl.models.requests.account_info import AccountInfo
    acct_info = AccountInfo(
        account=wallet.classic_address,
        ledger_index="validated",
        strict=True,
    )
    response = client.request(acct_info)

    print("response.status: ", response.status)

    import json
    print(json.dumps(response.result, indent=4, sort_keys=True))

def prepare_transaction(sender_wallet, amount, destination):
    import xrpl
    my_payment = xrpl.models.transactions.Payment(
        account = sender_wallet.classic_address,
        amount = xrpl.utils.xrp_to_drops(amount),
        destination = destination,
    )
    print("Payment object:", my_payment)