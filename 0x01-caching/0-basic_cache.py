#!/usr/bin/python3
""" BasicCache that inherits from BaseCaching """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''implement cache '''

    def __init__(self):
        '''init function'''
        super().__init__()

    def put(self, key, item):
        '''put in the cache dictionary'''
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        ''' get from  the cache dictionary'''
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
