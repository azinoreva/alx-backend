Caching Algorithms Project
Overview
This project involves implementing different caching algorithms using Python. The objective is to understand and implement various cache replacement policies: FIFO, LIFO, LRU, and MRU.

Project Files
base_caching.py

Defines the BaseCaching class. This base class provides a dictionary cache_data to store cache items and defines the methods put and get that must be implemented by subclasses.
0-basic_cache.py

Implements the BasicCache class, which is a basic caching system without a limit on the number of items. It inherits from BaseCaching.
1-fifo_cache.py

Implements the FIFOCache class, which uses the FIFO (First In, First Out) replacement policy. It discards the oldest item when the cache exceeds the maximum number of items allowed.
2-lifo_cache.py

Implements the LIFOCache class, which uses the LIFO (Last In, First Out) replacement policy. It discards the most recently added item when the cache exceeds the maximum number of items allowed.
3-lru_cache.py

Implements the LRUCache class, which uses the LRU (Least Recently Used) replacement policy. It discards the least recently used item when the cache exceeds the maximum number of items allowed.
4-mru_cache.py

Implements the MRUCache class, which uses the MRU (Most Recently Used) replacement policy. It discards the most recently used item when the cache exceeds the maximum number of items allowed.
