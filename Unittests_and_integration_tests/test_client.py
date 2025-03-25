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

        expected = "www.kevin.com"
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

        moi = {"name": "moi", "license": {"key": "a"}}
        toi = {"name": "toi", "license": {"key": "b"}}
        lui = {"name": "lui"}

        to_mock = "client.GithubOrgClient._public_repos_url"

        get_json_mock.return_value = [moi, toi, lui]

        with patch(to_mock, PropertyMock(return_value="www.kevin.com")) as y:
            x = GithubOrgClient("x")
            self.assertEqual(x.public_repos(), ["moi", "toi", "lui"])
            self.assertEqual(x.public_repos("a"), ["moi"])
            self.assertEqual(x.public_repos("c"), [])
            self.assertEqual(x.public_repos(2), [])
            get_json_mock.assert_called_once_with("www.kevin.com")
            y.assert_called_once_with()

    @parameterized.expand([
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ])
    def test_has_license(self, repo, license, expected):
        """
        Method tests the license checker
        """
        self.assertEqual(GithubOrgClient.has_license(
            repo, license), expected)


if __name__ == '__main__':
    unittest.main()
