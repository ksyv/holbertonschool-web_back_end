#!/usr/bin/env python3
"""
Log filter module
"""
import re  # Import the regular expressions module
from typing import List  # Import List for type annotations
import logging  # Import the logging module


PII_FIELDS = ("name", "email", "phone", "ssn", "password")  # Define PII fields


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Obfuscates specified fields in a log message.

    Args:
        fields: List of fields to obfuscate.
        redaction: Replacement string.
        message: Log message.
        separator: Field separator.

    Returns:
        The obfuscated log message.
    """
    # Use regular expression to replace specified fields
    return re.sub(r"("+separator+")(" + "|".join(fields)
                  + r")=([^"+separator+"]*)", r"\1\2="+redaction, message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class.
        """

    REDACTION = "***"  # Default replacement string
    # Log format
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"  # Default field separator

    def __init__(self, fields: List[str]):
        """Initializes the formatter with the fields to redact."""
        # Initialize parent formatter
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields  # Store fields to redact

    def format(self, record: logging.LogRecord) -> str:
        """Formats a log record by redacting sensitive fields."""
        # Format record with parent format
        message = super().format(record)
        # Redact sensitive fields in the formatted message
        return filter_datum(self.fields, self.REDACTION, message,
                            self.SEPARATOR)


def get_logger() -> logging.Logger:
    """
    Creates a logger with a stream handler and a redacting formatter.
    Returns:
        logging.Logger: The configured logger.
    """
    # Create a logger named "user_data"
    logger = logging.getLogger("user_data")
    # Set log level to INFO
    logger.setLevel(logging.INFO)
    # Prevent log propagation to parents
    logger.propagate = False
    # Create a stream handler (console)
    stream_handler = logging.StreamHandler()
    # Create a redacting formatter
    formatter = RedactingFormatter(PII_FIELDS)
    # Associate formatter with stream handler
    stream_handler.setFormatter(formatter)
    # Add stream handler to logger
    logger.addHandler(stream_handler)

    return logger  # Return the configured logger
