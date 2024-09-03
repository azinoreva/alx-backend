#!/usr/bin/env python3
"""
Defines a function named `index_range`
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    returns  a tuple of the start and end index for the given page
    """
    start_index = page * page_size
    return start_index - page_size, start_index
