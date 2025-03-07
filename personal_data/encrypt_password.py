#!/usr/bin/env python3
import bcrypt
'''
encrypt password modle
'''


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt.

    Args:
        password: The password to hash.

    Returns:
        The salted, hashed password as a byte string.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Checks if a password matches a hashed password using bcrypt.

    Args:
        hashed_password: The hashed password as a byte string.
        password: The password to check.

    Returns:
        True if the password matches the hashed password, False otherwise.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)


if __name__ == '__main__':
    password = "MyAmazingPassw0rd"
    encrypted_password = hash_password(password)
    print(encrypted_password)
    print(is_valid(encrypted_password, password))
