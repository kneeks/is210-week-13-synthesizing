#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Pickle Cache"""


import os
import pickle


class PickleCache(object):
    """Class for PickCache"""

    def __init__(self, file_path='datastore.pkl', autosync=False):
        """Constructor for PickCache

        Args:
            file_path(str): Path of the file, def = datastore.pkl
            autosync(bool): optional def = false

        Examples:
            >>> cacher = PickleCache()
            >>> kprint cacher._PickleCache__file_path
            'datastore.pkl'
            >>> print cacher._PickleCache__file_object
            None
            >>> print cacher._PickleCache__data
            {}

        Atributes:
            __file_path(str): Pseudo-private attribute*, assigned the
                constructor variable file_path value.
            __data(dict): Pseudo-private attribute, instantiated as an empty
                dictionary object
            autosync(bool): A non-private attribute
            """
        self.__file_path = file_path
        self.__data = {}
        self.autosync = autosync
        self.load()

    def __setitem__(self, key, value):
        """creates key and the value of key into a dict

        Args:
            key(mix): key of dict
            value(mix): value of key

        Returns:
            mix: value of key

        Examples:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print pcache._PickleCache__data['test']
            'hello'
        """
        self.__data[key] = value
        if self.autosync is True:
            self.flush()

    def __len__(self):
        """amount of data in a dict set

        Returns:
            num: of data in a dict

        Examples:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print pcache._PickleCache__data['test']
            'hello'
            >>> len(pcacher)
            1
       """
        len_data = len(self.__data)
        return len_data

    def __getitem__(self, key):
        """tests if key is in dict

        Args:
            key(mixed): key which is checked with dict key

        Returns:
            the value of the key if it exists or raises an error

        Examples:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print pcache['test']
            'hello'
        """
        try:
            if self.__data[key]:
                return self.__data[key]
        except (TypeError, KeyError) as error:
            raise error

    def __delitem__(self, key):
        """removes unwanted objects

        Args:
            key(mixed): key which is checked with dict key

        Examples:
            >>> pcache = PickleCache()
            >>> pcache['apple'] = 'banana'
            >>> print len(pcache)
            1
            >>> del pcache['apple']
            >>> print len(pcache)
            0
        """
        if self.__data[key]:
            del self.__data[key]
        if self.autosync is True:
            self.flush()

    def load(self):
        """
        Pickles and saves it to a file. This way the data can be accessed
        the next time the program runs.

        >>> import pickle
        >>> fh = open('datastore.pkl', 'w')
        >>> pickle.dump({'foo': 'bar'}, fh)
        >>> fh.close()
        >>> pcache = PickleCache('datastore.pkl')
        >>> print pcache['foo']
        'bar'
        """
        if os.path.exists(self.__file_path) and \
           os.path.getsize(self.__file_path) > 0:
            read_file = open(self.__file_path, 'r')
            self.__data = pickle.load(read_file)
            read_file.close()

    def flush(self):
        """cache is saved and stored

        Examples:
            >>> pcache = PickleCache()
            >>> pcache['foo'] = 'bar'
            >>> pcache.flush()
            >>> fhandler = open(pcache._PickleCache__file_path, 'r')
            >>> data = pickle.load(fhandler)
            >>> print data
            {'foo': 'bar'}
        """
        writefile = open(self.__file_path, 'w')
        pickle.dump(self.__data, writefile)
        writefile.close()
