#!/usr/bin/env python3

"""
Module to do caching 
"""

from baseCaching import BaseCaching 


class BaseCache(BaseCaching):
    def __init__(self) -> None:
        super().__init__()

    def put(self, key, item):
        """
        Args:
            key ([type]): [description]
            item ([type]): [description]

        Returns:
            [type]: [description]
        """
        if key  is not None and item is not None:
            self.cache_data[key] = item
            
    
    def get (self, key):
        """AI is creating summary for get

        Args:
            key ([type]): [description]
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
        

