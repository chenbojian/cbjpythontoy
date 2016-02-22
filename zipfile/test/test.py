import unittest
from unzipcomic import *


class MyTestCase(unittest.TestCase):
    def test_find_seven_zip(self):
        self.assertEqual(find_seven_zip(), r'C:\Program Files\7-Zip\7z.exe')

    def test_list_file_with_seven_zip(self):
        sz = SevenZip()
        print(sz.list_zipped_file('1.rar', '扶她奶茶'))
