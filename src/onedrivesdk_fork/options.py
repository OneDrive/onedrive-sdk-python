'''
------------------------------------------------------------------------------
 Copyright (c) 2015 Microsoft Corporation

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in
 all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 THE SOFTWARE.
------------------------------------------------------------------------------
'''


class Option(object):

    def __init__(self, key, value):
        """Initialize the Option, used for passing
        options into requests

        Args:
            key (str): The key for the option
            value (str): The value for the option

        """
        self._key = key
        self._value = value

    @property
    def key(self):
        """Gets and sets the key of the :class:`Option`

        Returns:
            str: The key"""
        return self._key

    @key.setter
    def key(self, value):
        self._key = value

    @property
    def value(self):
        """Gets and sets the value of the :class:`Option`

        Returns:
            str: The value"""
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class QueryOption(Option):
    """Option used for the query string of a request"""
    pass


class HeaderOption(Option):
    """Option used for the header of the request"""
    pass
