#!/usr/bin/env python3
"""Modul for test GithubOrgClient.org"""
import unittest
from parameterized import parameterized
from unittest.mock import Mock, patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Class to parameterize and patch as decorators
    """

    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True})
        ])
    @patch("client.get_json")
    def test_org(self, org, expected, get_patch):
        """Tests that GithubOrgClient.org returns the correct value"""
        get_patch.return_value = expected
        test = GithubOrgClient(org)
        self.assertEqual(test.org, expected)
        get_patch.assert_called_once_with("https://api.github.com/orgs/" + org)

    def test_public_repos_url(self):
        """
        Method tests that _public_repos_url works
        """

        expected = "www.yes.com"
        payload = {"repos_url": expected}
        to_mock = "client.GithubOrgClient.org"
        with patch(to_mock, PropertyMock(return_value=payload)):
            cli = GithubOrgClient("x")
            self.assertEqual(cli._public_repos_url, expected)


if __name__ == '__main__':
    unittest.main()
