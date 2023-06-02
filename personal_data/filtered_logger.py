#!/usr/bin/env python3
"""
Module that have a function called filter_datum that returns the log message
obfuscated
"""
from typing import List
import datetime
import re
import logging
import time


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Function called filter_datum that returns the log message obfuscated
    """
    for field in fields:
        message = re.sub("(?<={:s}=)(.*?)(?={:s})".format(field, separator),
                         redaction, message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Constructor """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Method to filter values in incoming log records using filter_datum
        """
        t = datetime.datetime.now()
        message = filter_datum(self.fields, RedactingFormatter.REDACTION,
                               record.msg, RedactingFormatter.SEPARATOR)
        message = logging.LogRecord(record.name, record.levelname, None, None,
                                    message, None, None)
        return super().format(message)
