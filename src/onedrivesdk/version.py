from __future__ import with_statement
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'version.txt'), encoding='utf-8') as f:
    __version__ = f.read()
