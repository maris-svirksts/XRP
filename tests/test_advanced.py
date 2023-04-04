# -*- coding: utf-8 -*-

from .context import basis

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(basis.account())

    def test_prepare_transaction(self):
        sender_client = basis.core.helpers.create_client()
        sender_wallet = basis.core.helpers.create_account(sender_client)

        receiver_client = basis.core.helpers.create_client()
        receiver_wallet = basis.core.helpers.create_account(receiver_client)

        basis.core.helpers.prepare_transaction(sender_wallet, 42, receiver_wallet.classic_address)


if __name__ == '__main__':
    unittest.main()
