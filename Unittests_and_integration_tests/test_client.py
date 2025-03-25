#!/usr/bin/env python3
"""Modul for test GithubOrgClient.org"""
import unittest
from parameterized import parameterized
from unittest.mock import Mock, patch
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


if __name__ == '__main__':
    unittest.main()
