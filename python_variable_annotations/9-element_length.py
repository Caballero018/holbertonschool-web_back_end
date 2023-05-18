#!/usr/bin/env python3
"""
Module containing an annotated function
"""
import typing


def element_length(lst: typing.Iterable[typing.Sequence])\
        -> typing.List[typing.Tuple[typing.Sequence, int]]:
    "Annotated function"
    return [(i, len(i)) for i in lst]
