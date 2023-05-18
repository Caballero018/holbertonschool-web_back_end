#!/usr/bin/env python3
"""
Module containing an annotated function make_multiplier that takes a
float multiplier as argument and returns a function that multiplies a
float by multiplier.
"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """
    Function make_multiplier that takes a float multiplier as argument and
    returns a function that multiplies a float by multiplier.
    """
    return lambda multi: multi * multiplier
