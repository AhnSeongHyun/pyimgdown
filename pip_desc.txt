pyimgdown is a python module for downloading image using url and resizing.


Installation
=============
pip install pyimgdown

Features
=============
* download image from url.
* resize and attach "_thumbnail" suffix.
* single url mode and file (url list file) mode.
* specify download directory.

Usage
=============
** url **

>>> import pyimgdown
>>> pyimgdown.download(url="https://pbs.twimg.com/profile_images/378800000492587949/2fa83be6eff4a9b113845aed83e8cf8e.jpeg")
...
{'image': '/Users/ahnseonghyun/PycharmProjects/PyImgDown/2fa83be6eff4a9b113845aed83e8cf8e.jpeg'}



** file **

>>> import pyimgdown
>>> pyimgdown.download(file="./url_list.txt")
...
[
  {'image': u'/Users/ahnseonghyun/PycharmProjects/PyImgDown/10502705036_25be7df97f.jpg'},
  {'image': u'/Users/ahnseonghyun/PycharmProjects/PyImgDown/8480728112_ecab467f54.jpg'},
  {'image': u'/Users/ahnseonghyun/PycharmProjects/PyImgDown/8326484656_6f5267010f.jpg'},
  {'image': u'/Users/ahnseonghyun/PycharmProjects/PyImgDown/8320741396_3153012a35.jpg'},
  {'image': u'/Users/ahnseonghyun/PycharmProjects/PyImgDown/8320725134_e739dbd1b3.jpg'},
  {'image': u'/Users/ahnseonghyun/PycharmProjects/PyImgDown/8319664711_eb897cc3f8.jpg'},
  {'image': u'/Users/ahnseonghyun/PycharmProjects/PyImgDown/8319663749_72c1cb12c0.jpg'},
  {'image': u'/Users/ahnseonghyun/PycharmProjects/PyImgDown/8319616643_83564ab041.jpg'},
  {'image': u'/Users/ahnseonghyun/PycharmProjects/PyImgDown/8320679860_b2a72bde7d.jpg'},
  {'image': u'/Users/ahnseonghyun/PycharmProjects/PyImgDown/8320679370_decc6fbb0e.jpg'}
]


** url+thumbnail**

>>> pyimgdown.download(url="https://pbs.twimg.com/profile_images/378800000492587949/2fa83be6eff4a9b113845aed83e8cf8e.jpeg", thumbnail_size=(64,64))
{
  'image': '/Users/ahnseonghyun/PycharmProjects/PyImgDown/2fa83be6eff4a9b113845aed83e8cf8e.jpeg',
  'thumbnail': '/Users/ahnseonghyun/PycharmProjects/PyImgDown/2fa83be6eff4a9b113845aed83e8cf8e_thumbnail.jpeg'
}


** url+thumbnail+download directory**

>>> pyimgdown.download(url="https://pbs.twimg.com/profile_images/378800000492587949/2fa83be6eff4a9b113845aed83e8cf8e.jpeg", thumbnail_size=(64,64), download_dir="./download")
{
  'image': './download/2fa83be6eff4a9b113845aed83e8cf8e.jpeg',
  'thumbnail': './download/2fa83be6eff4a9b113845aed83e8cf8e_thumbnail.jpeg'
}