#!/usr/bin/env python3
"""
Log filter module
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str):
    """
    Obfuscates specified fields in a log message.

    Args:
        fields: A list of strings representing the fields to obfuscate.
        redaction: A string representing the replacement value.
        message: The log message string.
        separator: The character separating the fields in the message.

    Returns:
        The obfuscated log message.
    """
    return re.sub(r"("+separator+")(" + "|".join(fields)
                  + r")=([^"+separator+"]*)", r"\1\2="+redaction, message)
