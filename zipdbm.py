'''
zipdbm
======
Dict-style DBM based on zipfile.
Unfortunately, you can't delete or overwrite files in zip archives.

    >>> import zipdbm
    >>> db = zipdbm.open('./test.zip')
    >>> db['foo'] = 'bar'
    >>> db['foo']
    'bar'
'''
from zipfile import ZipFile
from UserDict import DictMixin


__version__ = '1.0.0'


class ZipDBM(DictMixin):
    def __init__(self, filename):
        self.filename = filename

    def __getitem__(self, key):
        try:
            with ZipFile(self.filename, 'r') as z:
                return z.read(key)
        except IOError:
            raise KeyError(key)

    def __setitem__(self, key, value):
        if not isinstance(value, str):
            raise ValueError('%s value must be a string')
        with ZipFile(self.filename, 'a') as z:
            z.writestr(key, value)

    def keys(self):
        try:
            with ZipFile(self.filename, 'r') as z:
                return z.namelist()
        except IOError:
            return []


def open(filename):
    return ZipDBM(filename)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
