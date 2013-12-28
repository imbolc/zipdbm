zipdbm
======
Dict-style DBM based on zipfile.
Unfortunately, you can't delete or overwrite files in zip archives.

    >>> import zipdbm
    >>> db = zipdbm.open('./test.zip')
    >>> db['foo'] = 'bar'
    >>> db['foo']
    'bar'