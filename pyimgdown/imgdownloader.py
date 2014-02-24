# -*- coding: utf-8 -*-
#!/usr/bin/env python

__author__ = 'ahnseonghyun'

import urllib
import os
import urlparse

class ImageDownloader(object):

    def download(self, url=None, filename=None, download_dir=None):

        if not filename:
            filename = self.get_file_name(url)


        file_path = os.path.join(download_dir, filename)

        if url and filename:
            try:
                urllib.urlretrieve(url, file_path)
                return file_path
            except Exception as e:
                print e


    def get_file_name(self, url=None):
        # code from https://bitbucket.org/techtonik/python-wget/src
        fname = os.path.basename(urlparse.urlparse(url).path)
        if len(fname.strip(" \n\t.")) == 0:
            return None
        return fname


