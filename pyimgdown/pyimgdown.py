# -*- coding: utf-8 -*-
#!/usr/bin/env python

__author__ = 'ahnseonghyun'

import os
import sys
import codecs

from imgdownloader import ImageDownloader
from thumbnailer import Thumbnailer



global downloader
global thumbnailer


def do_work(url=None, download_dir=None):
    result_dict = dict()
    if url and download_dir:
        global downloader, thumbnailer
        dw_file_path = downloader.download(url=url, filename=None, download_dir=download_dir)

        thumbnail_file_path = None
        if thumbnailer:
            thumbnail_file_path = thumbnailer.thumbnail(image_file_path=dw_file_path, thumbnail_file_path=None)

        result_dict['image'] = dw_file_path

        if thumbnail_file_path:
            result_dict['thumbnail'] = thumbnail_file_path

        return result_dict

    else:
        raise Exception("url or download directory is None.")



def get_download_dir(download_dir=None):

    if download_dir:
        if not os.path.exists(download_dir):
            os.mkdir(download_dir)
    else:
        download_dir = os.path.dirname(os.path.abspath(__file__))

    return download_dir



def download(file=None, url=None, thumbnail_size=None, download_dir=None, thumbnail_file_suffix=None):

    download_dir = get_download_dir(download_dir)

    global downloader, thumbnailer
    downloader = ImageDownloader()
    thumbnailer = None

    if thumbnail_size:
        width = int(thumbnail_size[0])
        height = int(thumbnail_size[1])
        thumbnailer = Thumbnailer(width=width, height=height, thumbnail_file_suffix=thumbnail_file_suffix)


    if file:
        result_list = list()
        f = codecs.open(file, 'r', 'utf-8')
        url_list = f.readlines()

        for url in url_list:
            result_list.append(do_work(url=url.strip(), download_dir=download_dir))

        return result_list

    elif url:
        return do_work(url=url, download_dir=download_dir)
    else:
        print ("no arguments")
