#!/usr/bin/env python3
"""Modul for test GithubOrgClient.org"""
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import Mock, patch, PropertyMock, call
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos",
     "apache2_repos"), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration tests for github org client
    """

    @classmethod
    def setUpClass(cls):
        """
        Method pre-test
        """
        org = TEST_PAYLOAD[0][0]
        repos = TEST_PAYLOAD[0][1]
        org_mock = Mock()
        org_mock.json = Mock(return_value=org)
        cls.org_mock = org_mock
        repos_mock = Mock()
        repos_mock.json = Mock(return_value=repos)
        cls.repos_mock = repos_mock

        cls.get_patcher = patch("requests.get")
        cls.get = cls.get_patcher.start()

        options = {cls.org_payload["repos_url"]: repos_mock}
        cls.get.side_effect = lambda y: options.get(y, org_mock)

    @classmethod
    def tearDownClass(cls):
        """
        Method post-test
        """

        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Method tests public repos
        """

        y = GithubOrgClient("x")
        self.assertEqual(y.org, self.org_payload)
        self.assertEqual(y.repos_payload, self.repos_payload)
        self.assertEqual(y.public_repos(), self.expected_repos)
        self.assertEqual(y.public_repos("NONEXISTENT"), [])
        self.get.assert_has_calls(
            [call("https://api.github.com/orgs/x"),
             call(self.org_payload["repos_url"])]
        )

    def test_public_repos_with_license(self):
        """
        Method tests public repos
        """

        y = GithubOrgClient("x")
        self.assertEqual(y.org, self.org_payload)
        self.assertEqual(y.repos_payload, self.repos_payload)
        self.assertEqual(y.public_repos(), self.expected_repos)
        self.assertEqual(y.public_repos("NONEXISTENT"), [])
        self.assertEqual(y.public_repos("apache-2.0"), self.apache2_repos)
        self.get.assert_has_calls(
            [call("https://api.github.com/orgs/x"),
             call(self.org_payload["repos_url"])]
        )


if __name__ == '__main__':
    unittest.main()
