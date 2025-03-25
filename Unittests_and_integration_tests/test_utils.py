#!/usr/bin/env python3
"""Modul for test the access nested map function
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    """
    class for test access nested map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test that the method returns what it is supposed to."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
        ])
    def test_access_nested_map_exception(self, nested_map, path, not_expected):
        """test that a KeyError is raised"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(map, path)
            self.assertEqual(not_expected, context.exception)


class TestGetJson(unittest.TestCase):
    """class for test get_json function"""
    @parameterized.expand([
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ])
    def test_get_json(self, test_url, test_payload):
        """test that utils.get_json returns the expected result"""
        mock_res = Mock()
        mock_res.json.return_value = test_payload
        with patch("requests.get", return_value=mock_res):
            res = get_json(test_url)
            self.assertEqual(res, test_payload)

            mock_res.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """class for test memoize function"""
    def test_memoize(self):
        """test memoize function"""
        class TestClass:
            """intern test class"""
            def a_method(self):
                """always return 42"""
                return 42

            @memoize
            def a_property(self):
                """return memoize property"""
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42) as patched:
            test_class = TestClass()
            RealReturn = test_class.a_property

            self.assertEqual(RealReturn, 42)
            patched.assert_called_once()


if __name__ == '__main__':
    unittest.main()
