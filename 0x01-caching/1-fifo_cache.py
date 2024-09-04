#!/usr/bin/python3
"""
Module for FIFO Cache
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Cache class that inherits from BaseCaching"""

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.order = []  

    def put(self, key, item):
        """Assign the item value for the key in the cache data"""
        if key is not None and item is not None:
            if key in self.cache_data:
                
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                oldest_key = self.order.pop(0)
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")

            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Return the value linked to the key in the cache data"""
        return self.cache_data.get(key, None)

