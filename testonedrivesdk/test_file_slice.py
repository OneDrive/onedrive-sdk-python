import unittest
try:
    from unittest.mock import patch, mock_open
except ImportError:
    from mock import patch, mock_open

import io
import os
import math
import tempfile

from onedrivesdk.helpers.file_slice import FileSlice

class TestFileSlice(unittest.TestCase):
    def testSliceFileStartEnd(self):
        with tempfile.TemporaryFile() as f:
            f.write(b'123456789')
            f.flush()
            part = FileSlice(f, 0, 5)
            self.assertEqual(len(part), 5)
            self.assertEqual(part.read(), b'12345')
            self.assertEqual(part.read(3), b'')
            part.seek(0, io.SEEK_SET)
            self.assertEqual(part.read(3), b'123')
            self.assertEqual(part.tell(), 3)
            part.seek(-3, io.SEEK_CUR)
            self.assertEqual(part.tell(), 0)
            part.seek(-2, io.SEEK_END)
            self.assertEqual(part.tell(), 3)
            self.assertEqual(part.readall(), b'45')
            with self.assertRaises(IOError):
                part.write('abc')
            with self.assertRaises(IOError):
                part.writelines(['foo', 'bar'])

    def testSliceFileStartLength(self):
        with tempfile.TemporaryFile() as f:
            f.write(b'123456789')
            f.flush()
            part = FileSlice(f, 0, length=5)
            self.assertEqual(len(part), 5)
            self.assertEqual(part.read(), b'12345')
            self.assertEqual(part.read(3), b'')
            part.seek(0)
            self.assertEqual(part.read(3), b'123')
            self.assertEqual(part.tell(), 3)
            part.seek(-3, io.SEEK_CUR)
            self.assertEqual(part.readall(), b'12345')
            with self.assertRaises(IOError):
                part.write('abc')
            with self.assertRaises(IOError):
                part.writelines(['foo', 'bar'])

    def testSliceFileMiddleStartEnd(self):
        with tempfile.TemporaryFile() as f:
            f.write(b'123456789')
            f.flush()
            part = FileSlice(f, 1, 5)
            self.assertEqual(len(part), 4)
            self.assertEqual(part.read(3), b'234')
            self.assertEqual(part.readall(), b'5')
            self.assertEqual(part.read(), b'')
            self.assertEqual(part.tell(), 4)

    def testSliceFileMiddleStartLength(self):
        with tempfile.TemporaryFile() as f:
            f.write(b'123456789')
            f.flush()
            part = FileSlice(f, 1, length=5)
            self.assertEqual(len(part), 5)
            self.assertEqual(part.read(3), b'234')
            self.assertEqual(part.readall(), b'56')
            self.assertEqual(part.read(), b'')
            self.assertEqual(part.tell(), 5)

    def testSliceFileMiddleStartEnd_afterEOF(self):
        with tempfile.TemporaryFile() as f:
            f.write(b'123456789')
            f.flush()
            part = FileSlice(f, 8, 15)
            self.assertEqual(len(part), 1)
            self.assertEqual(part.read(3), b'9')
            self.assertEqual(part.readall(), b'')
            self.assertEqual(part.read(), b'')
            self.assertEqual(part.tell(), 1)
            part.seek(-1, io.SEEK_END)
            self.assertEqual(part.tell(), 0)
            self.assertEqual(part.readall(), b'9')

    def testSliceFileMiddleStartLength_afterEOF(self):
        with tempfile.TemporaryFile() as f:
            f.write(b'123456789')
            f.flush()
            part = FileSlice(f, 8, length=15)
            self.assertEqual(len(part), 1)
            self.assertEqual(part.read(3), b'9')
            self.assertEqual(part.readall(), b'')
            self.assertEqual(part.read(), b'')
            self.assertEqual(part.tell(), 1)
            part.seek(0)
            self.assertEqual(part.tell(), 0)
            self.assertEqual(part.readall(), b'9')


    def testSeek(self):
        with tempfile.TemporaryFile() as f:
            f.write(b'123456789')
            f.flush()
            part = FileSlice(f, 2, 7)
            part.seek(3)
            part.seek(part.tell(), io.SEEK_SET)
            self.assertEqual(part.tell(), 3)

    def testSanityChecks(self):
        with tempfile.TemporaryFile() as f:
            f.write(b'123456789')
            f.flush()
            with self.assertRaises(ValueError):
                part = FileSlice(f, -5, -2)
            with self.assertRaises(ValueError):
                part = FileSlice(f, 0, -2)
            with self.assertRaises(ValueError):
                part = FileSlice(f, -10, 2)
            with self.assertRaises(ValueError):
                part = FileSlice(f, 10, 2)
            with self.assertRaises(ValueError):
                part = FileSlice(f, 10, length=-2)

            part = FileSlice(f, 1, 5)
            with self.assertRaises(ValueError):
                part.seek(8)
            with self.assertRaises(ValueError):
                part.seek(8, io.SEEK_SET)
            part.seek(3)
            with self.assertRaises(ValueError):
                part.seek(4, io.SEEK_CUR)
            with self.assertRaises(ValueError):
                part.seek(-5, io.SEEK_END)

if __name__ == '__main__':
    unittest.main()
