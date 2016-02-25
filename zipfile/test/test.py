import shutil
import unittest

from sevenzip import *


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.sz = SevenZip()

    def test_find_seven_zip(self):
        self.assertEqual(self.sz.exe, r'C:\Program Files\7-Zip\7z.exe')

    def test_list_file_with_seven_zip(self):
        return_code = self.sz.list('1.rar', '扶她奶茶')
        self.assertEqual(return_code, 0)

    def test_unzip_file_with_seven_zip(self):
        self.assertFalse(Path('tmp').exists())
        return_code = self.sz.unzip('1.rar', '扶她奶茶', 'tmp')
        self.assertEqual(return_code, 0)
        self.assertTrue(Path('tmp').exists())
        shutil.rmtree('tmp')
