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

    @patch("client.get_json")
    def test_public_repos(self, get_json_mock):
        """
        Method tests the public repos
        """

        jeff = {"name": "Jeff", "license": {"key": "a"}}
        bobb = {"name": "Bobb", "license": {"key": "b"}}
        suee = {"name": "Suee"}

        to_mock = "client.GithubOrgClient._public_repos_url"

        get_json_mock.return_value = [jeff, bobb, suee]

        with patch(to_mock, PropertyMock(return_value="www.yes.com")) as y:
            x = GithubOrgClient("x")
            self.assertEqual(x.public_repos(), ["Jeff", "Bobb", "Suee"])
            self.assertEqual(x.public_repos("a"), ["Jeff"])
            self.assertEqual(x.public_repos("c"), [])
            self.assertEqual(x.public_repos(45), [])
            get_json_mock.assert_called_once_with("www.yes.com")
            y.assert_called_once_with()


if __name__ == '__main__':
    unittest.main()
