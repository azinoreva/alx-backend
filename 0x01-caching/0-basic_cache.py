#!/usr/bin/env python3

"""
Module to do caching 
"""


from base_caching import BaseCaching 


class BaseCache(BaseCaching):
    '''A class `BasicCache` that inherits from `BaseCaching`
       and is a caching system
    '''
    def put (self, key, item):
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
        return self.cache_data.get(key, None)
