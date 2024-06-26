#!/usr/bin/python3
""" LIFOCache that inherits from BaseCaching """
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    '''implement cache '''

    def __init__(self):
        '''init function'''
        super().__init__()

    def put(self, key, item):
        '''put in the cache dictionary'''
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
             and key not in self.cache_data.keys():
                l_key, l_value = self.cache_data.popitem()
                print("DISCARD: {}". format(l_key))

            self.cache_data[key] = item

    def get(self, key):
        ''' get from  the cache dictionary'''
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
