#!/usr/bin/env python3
"""
Defines a function named `index_range`
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    returns  a tuple of the start and end index for the given page
    """
    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)
