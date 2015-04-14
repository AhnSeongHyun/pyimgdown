# -*- coding:utf-8 -*-
__author__ = 'ahnseonghyun'


import unittest
import os
import sys
import pyimgdown
import codecs
try:
    import urlparse
except Exception as e:
    from urllib import parse as urlparse



class TestPyImgDown(unittest.TestCase):

    img_url = None



    def test_file(self):

        #crete test list
        test_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test1.txt')
        f = codecs.open(test_file_path, 'r', 'utf-8')
        url_list = f.readlines()
        file_path_list = list()

        for url in url_list:
            file_name = os.path.basename(urlparse.urlparse(url).path)
            file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
            file_path_list.append(file_path)


        result_list = pyimgdown.download(file=test_file_path)

        for result in result_list:
            download_file_path = result['image']

            if download_file_path in file_path_list:
                self.assertEquals
            else:
                self.assertNotEquals
    #
    def test_file_thumbnail(self):

        thumbnail_size = (64, 64)

        #crete test list
        test_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test2.txt')
        f = codecs.open(test_file_path, 'r', 'utf-8')
        url_list = f.readlines()

        file_path_list = list()
        thumbnail_file_path_list = list()


        for url in url_list:
            file_name = os.path.basename(urlparse.urlparse(url).path)
            file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
            file_path_list.append(file_path)

            name, extension = os.path.splitext(file_name)
            thumbnail_file_name = name + "_thumbnail" + extension
            thumbnail_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), thumbnail_file_name)

            thumbnail_file_path_list.append(thumbnail_file_path)


        result_list = pyimgdown.download(file=test_file_path, thumbnail_size=thumbnail_size)

        for result in result_list:
            download_file_path = result['image']
            thumbnail_file_path = result['thumbnail']

            if download_file_path in file_path_list:
                self.assertEquals
            else:
                self.assertNotEquals

            if thumbnail_file_path in thumbnail_file_path_list:
                self.assertEquals
            else:
                self.assertNotEquals


    def test_file_thumbnail_dir(self):

        thumbnail_size = (64, 64)
        download_dir = "./dump"

        #crete test list
        test_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test3.txt')
        f = codecs.open(test_file_path, 'r', 'utf-8')
        url_list = f.readlines()

        file_path_list = list()
        thumbnail_file_path_list = list()


        for url in url_list:
            file_name = os.path.basename(urlparse.urlparse(url).path)
            file_path = os.path.join(download_dir, file_name)
            file_path_list.append(file_path)

            name, extension = os.path.splitext(file_name)
            thumbnail_file_name = name + "_thumbnail" + extension
            thumbnail_file_path = os.path.join(download_dir, thumbnail_file_name)

            thumbnail_file_path_list.append(thumbnail_file_path)


        result_list = pyimgdown.download(file=test_file_path, thumbnail_size=thumbnail_size, download_dir=download_dir)

        for result in result_list:
            download_file_path = result['image']
            thumbnail_file_path = result['thumbnail']

            if download_file_path in file_path_list:
                self.assertEquals
            else:
                self.assertNotEquals

            if thumbnail_file_path in thumbnail_file_path_list:
                self.assertEquals
            else:
                self.assertNotEquals

    def test_file_thumbnail_suffix_none(self):

        thumbnail_size = (64, 64)
        download_dir = "./dump"

        #crete test list
        test_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test4.txt')
        f = codecs.open(test_file_path, 'r', 'utf-8')
        url_list = f.readlines()

        file_path_list = list()
        thumbnail_file_path_list = list()

        result_list = pyimgdown.download(file=test_file_path, \
                                        thumbnail_size=thumbnail_size,\
                                        download_dir=download_dir, \
                                        thumbnail_file_suffix=None)

        for result in result_list:
            download_file_path = result['image']
            thumbnail_file_path = result['thumbnail']


            if "_thumbnail" in thumbnail_file_path:
                self.assertEquals
            else:
                self.assertNotEquals

    def test_file_thumbnail_suffix(self):

        thumbnail_size = (64, 64)
        download_dir = "./dump"

        #crete test list
        test_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test5.txt')
        f = codecs.open(test_file_path, 'r', 'utf-8')
        url_list = f.readlines()

        file_path_list = list()
        thumbnail_file_path_list = list()


        result_list = pyimgdown.download(file=test_file_path, \
                                        thumbnail_size=thumbnail_size,\
                                        download_dir=download_dir, \
                                        thumbnail_file_suffix="_thumb")

        for result in result_list:
            download_file_path = result['image']
            thumbnail_file_path = result['thumbnail']


            if "_thumb" in thumbnail_file_path:
                self.assertEquals
            else:
                self.assertNotEquals

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPyImgDown)
    unittest.TextTestRunner(verbosity=2).run(suite)
 