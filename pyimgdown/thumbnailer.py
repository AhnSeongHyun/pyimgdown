# -*- coding: utf-8 -*-
#!/usr/bin/env python

__author__ = 'ahnseonghyun'

import os
from wand.image import Image

class Thumbnailer(object):

    width = 64
    height = 64

    thumbnail_file_suffix = "_thumbnail"

    def __init__(self):
        pass

    def __init__(self, width=64, height=64, thumbnail_file_suffix=None):
        self.width = width
        self.height = height

        if thumbnail_file_suffix:
            self.thumbnail_file_suffix = thumbnail_file_suffix


    def thumbnail(self, image_file_path=None, thumbnail_file_path=None):

        if not thumbnail_file_path:
            thumbnail_file_path = self.get_thumbnail_file_path(file_path=image_file_path)

        try:
            img = Image(filename=image_file_path)
            img.resize(self.width, self.height)
            img.save(filename=thumbnail_file_path)

            return thumbnail_file_path

        except Exception as e:
            print "Unable to load image"
            return None


    def get_thumbnail_file_path(self, file_path=None):

        if file_path:
            file_name = os.path.basename(file_path)
            name, extension = os.path.splitext(file_name)
            thumbnail_file_name = name + self.thumbnail_file_suffix + extension

            return os.path.join(os.path.dirname(file_path), thumbnail_file_name)

        else:
            raise Exception("no file path")