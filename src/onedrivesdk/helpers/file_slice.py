# -*- coding: utf-8 -*-
'''
The MIT License (MIT)

Copyright (c) 2015 Wiktor Niesiobędzki

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

import io
import os

class FileSlice(io.RawIOBase):
    '''
    This class represents a window over a file handle. It will allow only access
    and read of bytes above start and no further than end/length bytes
    '''
    def __init__(self, handle, start, end=None, length=None):
        '''
        Creates new instance of FileSlice on file-like object handle. It behaves
        like normal file object, but only allow reading of bytes above start and
        no further than end/lenght byte

        Args:
            handle (file-like object): file handle object to create a view over.
                File should be open in binary mode
            start (int): start byte number, makring the first byte that can be
                read from FileSlice
            end (int): Optional. Last byte of the file that can be read.
            length (int): Optional. Number of the bytes, starting from the
                start, that can be read from FileSlice

            One of end or length must be provided
        '''
        assert end or length, "You need to provide one of end or length parameter"
        assert not (end and length), "You need to proivde only one parameter: end or length, not both"
        if start < 0:
            raise ValueError("Start of the file smaller than 0")
        if end and end < start:
            raise ValueError("End of the tile smaller than start")
        if length and length < 0:
            raise ValueError("Length smaller than 0")

        self._handle = handle
        self._start = start
        if end:
            self._end = end
        else:
            self._end = start + length
        self._end = min(self._end, os.fstat(handle.fileno()).st_size)
        self.seek(0)

    @property
    def _bytes_left(self):
        current_pos = self._handle.tell()
        return self._end - current_pos

    def close(self):
        # do nothing, someone else might want to process this file
        return

    @property
    def closed(self):
        return self._handle.closed

    def fileno(self):
        return self._handle.fileno()

    def flush(self):
        return self._handle.flush()

    def len(self):
        # this is provided for requests, so it will properly recognize the size of the file
        return self._bytes_left

    def __len__(self):
        # this is provided for requests, so it will properly recognize the size of the file
        return self.len()

    def isatty(self):
        return self._handle.isatty()

    def readable(self):
        return self._handle.readable()

    def read(self, size=-1):
        if size == -1:
            read_size = self._bytes_left
        else:
            read_size = min(size, self._bytes_left)
        return self._handle.read(read_size)

    def readall(self):
        return self._handle.read(self._bytes_left)

    def readinto(self, b):
        if len(b) > self._bytes_left:
            r = self._handle.read(self._bytes_left)
            b[:len(r)] = r
            return len(r)
        return self._handle.readinto(b)

    def readline(self, size=-1):
        return self._handle.readline(max(size, self._bytes_left))

    def readlines(self, hint=-1):
        return self._handle.readlines(max(hint, self._bytes_left))

    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            desired_pos = self._start + offset
        if whence == io.SEEK_CUR:
            desired_pos = self._handle.tell() + offset
        if whence == io.SEEK_END:
            desired_pos = self._end + offset

        if desired_pos < self._start:
            raise ValueError("Seeking before the file slice")
        if desired_pos > self._end:
            raise ValueError("Seekeing past the end of file slice")

        ret = self._handle.seek(desired_pos, io.SEEK_SET)
        if ret:
            return ret - self._start
        else:
            return ret

    def seekable(self):
        return self._handle.seekable()

    def tell(self):
        return self._handle.tell() - self._start

    def truncate(self, size=None):
        raise IOError("Operation not supported")

    def writable(self):
        return False

    def write(self, b):
        raise IOError("Operation not supported")

    def writelines(self, lines):
        raise IOError("Operation not supported")

