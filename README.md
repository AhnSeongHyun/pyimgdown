pyimgdown is a python module for downloading image using url and resizing.

[![Build Status](https://travis-ci.org/AhnSeongHyun/pyimgdown.png)](https://travis-ci.org/AhnSeongHyun/pyimgdown)


Installation
=============
    pip install pyimgdown


Features
=============
* download image from url.
* resize and attach thumbnail file suffix.
* single url mode and file (url list file) mode.
* specify download directory.

Python Version
==============
* support python 2.7 

Usage
=============

**url**

    > import pyimgdown
    > url = "https://localhost/test.jpeg"
    > pyimgdown.download(url=url)
    ...
    => {'image': './PyImgDown/test.jpeg'}




**file**

    > import pyimgdown<br/>
    > pyimgdown.download(file="./url_list.txt")<br/>
    ...
    [
    {'image': u'./PyImgDown/test1.jpg'},
    {'image': u'./PyImgDown/test2.jpg'},
    {'image': u'./PyImgDown/test3.jpg'},
    {'image': u'./PyImgDown/test4.jpg'},
    {'image': u'./PyImgDown/test5.jpg'},
    {'image': u'./PyImgDown/test6.jpg'},
    {'image': u'./PyImgDown/test7.jpg'},
    {'image': u'./PyImgDown/test8.jpg'},
    {'image': u'./PyImgDown/test9.jpg'},
    {'image': u'.PyImgDown/test10.jpg'}
    ]


**url+thumbnail**

    > pyimgdown.download(url="https://localhost/test.jpeg", thumbnail_size=(64,64))
    {
    'image': './PyImgDown/test.jpeg',
    'thumbnail': './PyImgDown/test_thumbnail.jpeg'
    }


**url+thumbnail+download directory**

    > pyimgdown.download(url="https://localhost/test.jpeg", thumbnail_size=(64,64), download_dir="./download")
    {
    'image': './download/test.jpeg',
    'thumbnail': './download/test_thumbnail.jpeg'
    }


**url+thumbnail+download directory+thumbnail_file_suffix**


    > pyimgdown.download(url="https://localhost/test.jpeg", thumbnail_size=(64,64), download_dir="./download", thumbnail_file_suffix="_thumb")
    {
    'image': './download/test.jpeg',
    'thumbnail': './download/test_thumb.jpeg'
    }