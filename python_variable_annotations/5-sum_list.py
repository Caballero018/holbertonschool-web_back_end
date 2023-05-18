#!/usr/bin/env python3
"""
Module containing an annotated function sum_list which takes a list
input_list of floats as argument and returns their sum as a float.
"""
import typing


def sum_list(input_list: typing.List[float]) -> float:
    """
    Function sum_list which takes a list input_list of floats as argument
    and returns their sum as a float.
    """
    n = 0.0
    for input in input_list:
        n += input
    return n
