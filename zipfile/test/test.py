import shutil
import unittest

from unzipcomic import *


class MyTestCase(unittest.TestCase):
    def test_find_seven_zip(self):
        self.assertEqual(find_seven_zip(), r'C:\Program Files\7-Zip\7z.exe')

    def test_list_file_with_seven_zip(self):
        sz = SevenZip()
        output = sz.list_zipped_file('1.rar', '扶她奶茶')
        self.assertTrue(len(output) > 0)

    def test_unzip_file_with_seven_zip(self):
        self.assertFalse(Path('tmp').exists())
        sz = SevenZip()
        output = sz.unzip_zipped_file('1.rar', '扶她奶茶', 'tmp')
        self.assertTrue(len(output) > 0)
        self.assertTrue(Path('tmp').exists())
        shutil.rmtree('tmp')
