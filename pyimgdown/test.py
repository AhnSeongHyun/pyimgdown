# -*- coding:utf-8 -*-
__author__ = 'ahnseonghyun'


import unittest
import os
import sys
import pyimgdown
import codecs
import urlparse

class TestPyImgDown(unittest.TestCase):

    img_url = None
    def setUp(self):
        self.file = "test.txt"
        self.url = "https://pbs.twimg.com/profile_images/378800000492587949/2fa83be6eff4a9b113845aed83e8cf8e.jpeg"

    def test_url(self):
        file_name = "2fa83be6eff4a9b113845aed83e8cf8e.jpeg"
        if os.path.isfile(file_name):
            os.remove(file_name)

        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)

        result = pyimgdown.download(url=self.url)
        self.assertEqual(result['image'], file_path)


    def test_url_thumbnail(self):
        file_name = "2fa83be6eff4a9b113845aed83e8cf8e.jpeg"
        thumbnail_file_name = "2fa83be6eff4a9b113845aed83e8cf8e_thumbnail.jpeg"

        if os.path.isfile(file_name):
            os.remove(file_name)

        if os.path.isfile(thumbnail_file_name):
            os.remove(thumbnail_file_name)

        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
        thumbnail_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), thumbnail_file_name)

        thumbnail_size = (64, 64)
        result = pyimgdown.download(url=self.url, thumbnail_size=thumbnail_size)

        self.assertEqual(result['image'], file_path)
        self.assertEqual(result['thumbnail'], thumbnail_file_path)


    def test_url_thumbnail_dir(self):
        thumbnail_size = (64, 64)
        download_dir = "./dump"

        file_name = "2fa83be6eff4a9b113845aed83e8cf8e.jpeg"
        thumbnail_file_name = "2fa83be6eff4a9b113845aed83e8cf8e_thumbnail.jpeg"

        file_path = os.path.join(download_dir, file_name)
        thumbnail_file_path = os.path.join(download_dir, thumbnail_file_name)

        if os.path.isfile(file_path):
            os.remove(file_path)

        if os.path.isfile(thumbnail_file_path):
            os.remove(thumbnail_file_path)

        result = pyimgdown.download(url=self.url, thumbnail_size=thumbnail_size, download_dir=download_dir)

        self.assertEqual(result['image'], file_path)
        self.assertEqual(result['thumbnail'], thumbnail_file_path)


    def test_file(self):

        #crete test list
        test_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), self.file)
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

    def test_file_thumbnail(self):

        thumbnail_size = (64, 64)

        #crete test list
        test_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), self.file)
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
        test_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), self.file)
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


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPyImgDown)
    unittest.TextTestRunner(verbosity=2).run(suite)
