"""Tests for certbot_dns_dnsimple.dns_dnsimple."""

import unittest

import mock
from requests.exceptions import HTTPError

from certbot.compat import os
from certbot.plugins import dns_test_common
from certbot.plugins import dns_test_common_lexicon
from certbot.tests import util as test_util

API_ID = 12345
API_TOKEN = 'foo'


class AuthenticatorTest(test_util.TempDirTestCase,
                        dns_test_common_lexicon.BaseLexiconAuthenticatorTest):

    def setUp(self):
        super(AuthenticatorTest, self).setUp()

        from certbot_dns_verifier.dns_verifier import Authenticator

        path = os.path.join(self.tempdir, 'file.ini')
        dns_test_common.write({"verifier_api_id": API_ID, "verifier_api_token": API_TOKEN}, path)

        self.config = mock.MagicMock(verifier_credentials=path,
                                     verifier_propagation_seconds=0)  # don't wait during tests

        self.auth = Authenticator(self.config, "verifier")

        self.mock_client = mock.MagicMock()
        # _get_dnsimple_client | pylint: disable=protected-access
        self.auth._get_dns_client = mock.MagicMock(return_value=self.mock_client)


class DNSimpleLexiconClientTest(unittest.TestCase, dns_test_common_lexicon.BaseLexiconClientTest):

    LOGIN_ERROR = HTTPError('401 Client Error: Unauthorized for url: ...')

    def setUp(self):
        from certbot_dns_verifier.dns_verifier import _DNSLexiconClient

        self.client = _DNSLexiconClient(API_ID, API_TOKEN, 0)

        self.provider_mock = mock.MagicMock()
        self.client.provider = self.provider_mock


if __name__ == "__main__":
    unittest.main()  # pragma: no cover