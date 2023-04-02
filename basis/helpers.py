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
    test_wallet = generate_faucet_wallet(client, debug=True)

    # Return an account str from the wallet
    return test_wallet.classic_address

# Derive an x-address from the classic address:
# https://xrpaddress.info/
def print_addresses(account):
    from xrpl.core import addresscodec
    test_xaddress = addresscodec.classic_address_to_xaddress(account, tag=12345, is_test_network=True)
    print("\nClassic address:\n\n", account)
    print("X-address:\n\n", test_xaddress)

# Look up info about your account
def print_account_info(client, client_account):
    from xrpl.models.requests.account_info import AccountInfo
    acct_info = AccountInfo(
        account=client_account,
        ledger_index="validated",
        strict=True,
    )
    response = client.request(acct_info)

    print("response.status: ", response.status)

    import json
    print(json.dumps(response.result, indent=4, sort_keys=True))