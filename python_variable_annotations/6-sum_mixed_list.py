#!/usr/bin/env python3
"""
Module containing an annotated function sum_mixed_list which takes a
list mxd_lst of integers and floats and returns their sum as a float.
"""
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """
    Function sum_mixed_list which takes a list mxd_lst of integers
    and floats and returns their sum as a float.
    """
    number = 0.0
    for n in mxd_lst:
        number += n
    return number
