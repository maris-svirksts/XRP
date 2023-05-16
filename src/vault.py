import hvac

def load_secret_key_from_vault(vault_url: str, vault_token: str, vault_path: str) -> str:
    client = hvac.Client(url=vault_url, token=vault_token)
    response = client.secrets.kv.v2.read_secret_version(path=vault_path)
    secret_key = response['data']['data']['secret_key']
    return secret_key
