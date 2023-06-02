#!/usr/bin/env python3
"""
Module that have a function called filter_datum that returns the log message
obfuscated
"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Function called filter_datum that returns the log message obfuscated
    """
    for field in fields:
        message = re.sub("(?<={:s}=)(.*?)(?={:s})".format(field, separator),
                         redaction, message)
    return message
