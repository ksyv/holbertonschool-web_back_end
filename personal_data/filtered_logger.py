#!/usr/bin/env python3
"""
Log filter module
"""
import re  # Import the regular expressions module
from typing import List  # Import List for type annotations
import logging  # Import the logging module
import os
import mysql.connector




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

def get_db():
    """Retrieves a database connection."""
    # Step 2: Retrieve database credentials from environment variables.
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    database = os.getenv("PERSONAL_DATA_DB_NAME")

    # Step 3: Check if the database name is set, if not return None
    if not database:
        return None

    # Step 4: Establish a database connection and error handling.
    try:
        connection = mysql.connector.connect(
            user=username,
            password=password,
            host=host,
            database=database,
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to database: {err}")
        return None

#Example of how to use the function.
if __name__ == "__main__":
    db_connection = get_db()
    if db_connection:
        print("Database connection successful!")
        # Perform database operations here...
        db_connection.close() #close connection when finished.
    else:
        print("Database connection failed.")


PII_FIELDS = ("name", "email", "phone", "ssn", "password")  # Define PII fields
