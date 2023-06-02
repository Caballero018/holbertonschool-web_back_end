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
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        t = datetime.datetime.now()
        message = filter_datum(self.fields, RedactingFormatter.REDACTION, record.msg, RedactingFormatter.SEPARATOR)
        message = RedactingFormatter.FORMAT % {'name': record.name, 'levelname': record.levelname, 'asctime': '2019-11-19 18:24:25,105', 'message': message}
        return message
