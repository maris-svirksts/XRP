# -*- coding: utf-8 -*-
from basis import helpers

def account():
    """Initiate..."""
    client = helpers.create_client()
    account = helpers.create_account(client)

    helpers.print_addresses(account)
    helpers.print_account_info(client, account)

